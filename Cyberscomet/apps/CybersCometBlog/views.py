from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category, Tag, Comment, CommentForm, Notice, MessageForm, Message
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown
from apps.CybersCometBlog.tracking_view import user_tracking


# Create your views here.
@user_tracking
def index(request):
    try:
        top_index_articles = Article.objects.filter(show_on_top_index_or_not=1)
        index_articles = Article.objects.filter(show_on_index_or_not=1)
        notices = Notice.objects.filter(show_on_index_or_not=1)[:1]
        order_articles = Article.objects.order_by('-publish_time')[:5]
        categories = Category.objects.filter()
        tags = Tag.objects.filter()
        messages = Message.objects.filter(show_on_index_or_not=1).order_by('-publish_time')
    except:
        return HttpResponse('首页没有article展示...请检查设置')
    return render(request, 'index.html', locals())


@user_tracking
def article_list(request, page_id):
    try:
        articles = Article.objects.filter()
        paginator = Paginator(articles, 5)
        notices = Notice.objects.filter(show_on_index_or_not=1)[:1]
        order_articles = Article.objects.order_by('-publish_time')[:5]
        categories = Category.objects.filter()
        tags = Tag.objects.filter()
        try:
            article_list = paginator.page(page_id)
        except PageNotAnInteger:
            article_list = paginator.page(page_id)
        except EmptyPage:
            article_list = paginator.page(paginator.num_pages)
        return render(request, 'article_list.html', locals())
    except:
        return render(request, 'article_list.html', locals())


@user_tracking
def article_detail(request, article_id):
    try:
        result = 0
        article = get_object_or_404(Article, pk=article_id)
        article.content = markdown.markdown(article.content,
                                            extensions=[
                                                'markdown.extensions.extra',
                                                'markdown.extensions.codehilite',
                                                'markdown.extensions.toc',
                                            ])
        article_tags = Tag.objects.filter(article=article_id)
        article_comments = Comment.objects.filter(reply_article_id=article_id)

        notices = Notice.objects.filter(show_on_index_or_not=1)[:1]
        order_articles = Article.objects.order_by('-publish_time')[:5]
        categories = Category.objects.filter()
        tags = Tag.objects.filter()

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment_content = comment_form.cleaned_data['content']
                comment_publisher_name = comment_form.cleaned_data['publisher_name']
                try:
                    new_comment = Comment.objects.create()
                    new_comment.content = comment_content
                    new_comment.publisher_name = comment_publisher_name
                    new_comment.reply_article_id = article_id
                    new_comment.save()
                    result = 1  # 成功创建评论

                    return render(request, 'article_detail.html', locals())
                except:
                    return render(request, 'article_detail.html', locals())
        return render(request, 'article_detail.html',
                      locals())
    except:
        return HttpResponse('网页渲染失败，请联系Cyberscomet')


def category(request, category_id):
    return render(request, 'category.html', locals())


@user_tracking
def about(request):
    try:
        notices = Notice.objects.filter(show_on_index_or_not=1)[:1]
        order_articles = Article.objects.order_by('-publish_time')[:5]
        categories = Category.objects.filter()
        tags = Tag.objects.filter()

        if request.method == 'POST':
            message_form = MessageForm(request.POST)
            if message_form.is_valid():
                message_name = message_form.cleaned_data['name']
                message_email = message_form.cleaned_data['email']
                message_phone = message_form.cleaned_data['phone']
                message_content = message_form.cleaned_data['content']
                try:
                    new_message = Message.objects.create()
                    new_message.name = message_name
                    new_message.email = message_email
                    new_message.phone = message_phone
                    new_message.content = message_content
                    new_message.save()
                    result = 1  # 成功创建留言

                    return render(request, 'about.html', locals())
                except:
                    return render(request, 'about.html', locals())
        return render(request, 'about.html', locals())
    except:
        return HttpResponse('网页渲染失败，请联系Cyberscomet')
