from django.contrib import admin
from .models import Article
from .models import Tag
from .models import Category
from .models import Comment
from .models import Notice
from .models import Message
from .models import UserIP
from .models import VisitNumber
from .models import DayNumber


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publish_time', 'category', 'show_on_index_or_not', 'show_on_top_index_or_not']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'publisher_name', 'publish_time', 'reply_article_id']


class NoticeAdmin(admin.ModelAdmin):
    list_display = ['content', 'publish_time', 'show_on_index_or_not']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'content', 'publish_time', 'show_on_index_or_not']


class UserIPAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'ip_location', 'end_point', 'time']


class VisitNumberAdmin(admin.ModelAdmin):
    list_display = ['count']


class DayNumberAdmin(admin.ModelAdmin):
    list_display = ['day', 'count']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(UserIP, UserIPAdmin)
admin.site.register(VisitNumber, VisitNumberAdmin)
admin.site.register(DayNumber, DayNumberAdmin)
admin.site.site_header = 'CybersComet后台管理'
admin.site.site_title = 'Cyberscomet后台管理'
