from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('article_list/<int:page_id>', views.article_list),
    path('article_detail/<int:article_id>', views.article_detail),
    path('category/<int:category_id>', views.category),
    path('about/', views.about),
]
