from django.db import models
from mdeditor.fields import MDTextField
from django import forms
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='分类名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField(max_length=100, verbose_name='内容')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    publisher_name = models.CharField(max_length=50, verbose_name='评论者姓名', default='路过的小同志')
    reply_article_id = models.CharField(max_length=20, verbose_name='回复文章ID', default='0')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class CommentForm(forms.Form):
    content = forms.CharField(label='内容', max_length=150,
                              widget=forms.Textarea(attrs={'class': 'form-control'}))
    publisher_name = forms.CharField(label='昵称', max_length=50, required=False,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    author = models.CharField(max_length=50, verbose_name='作者')
    description = models.CharField(max_length=200, verbose_name='摘要')
    thumbnail = models.URLField(verbose_name='链接')
    main_photo_link = models.CharField(max_length=200, verbose_name='主图片地址', default='None')
    content = MDTextField(verbose_name='内容')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    comment = models.ManyToManyField(Comment, verbose_name='评论', blank=True)
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    show_on_index_or_not = models.BooleanField(default=False, verbose_name='是否在首页显示')
    show_on_top_index_or_not = models.BooleanField(default=False, verbose_name='是否在轮播显示')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Notice(models.Model):
    content = models.TextField(max_length=100, verbose_name='内容')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    show_on_index_or_not = models.BooleanField(default=False, verbose_name='是否在首页显示')

    class Meta:
        verbose_name = '通知'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Message(models.Model):
    name = models.CharField(max_length=50, verbose_name='发布者姓名', default='路过的小同志')
    email = models.EmailField(max_length=40, default='example@xxx.com', verbose_name='邮箱地址')
    phone = models.CharField(max_length=20, default='10086', verbose_name='电话号码')
    content = models.TextField(max_length=150, verbose_name='内容')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    show_on_index_or_not = models.BooleanField(default=True, verbose_name='是否在首页显示')

    class Meta:
        verbose_name = '微言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class MessageForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=50, required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='邮箱', max_length=40, required=False,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='电话', max_length=20, required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='内容', max_length=150,
                              widget=forms.Textarea(attrs={'class': 'form-control'}))


class UserIP(models.Model):
    ip_address = models.CharField(max_length=30, verbose_name='IP地址')
    ip_location = models.CharField(max_length=30, verbose_name='地区')
    end_point = models.CharField(default='/', max_length=30, verbose_name='最终节点')
    time = models.DateTimeField(auto_now_add=True, verbose_name='访问时间')

    class Meta:
        verbose_name = '访客统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip_address


# 网站总访问次数
class VisitNumber(models.Model):
    count = models.IntegerField(default=0, verbose_name='网站总访问次数')  # 网站访问总次数

    class Meta:
        verbose_name = '网站总访问次数'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.count


# 单日访问量统计
class DayNumber(models.Model):
    day = models.DateField(default=timezone.now, verbose_name='单日访问量统计')
    count = models.IntegerField(default=0)  # 网站访问总次数

    class Meta:
        verbose_name = '单日访问量统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.day
