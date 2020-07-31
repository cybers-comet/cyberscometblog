# Generated by Django 3.0.8 on 2020-07-29 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CybersCometBlog', '0010_delete_commentform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, verbose_name='内容')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('show_on_index_or_not', models.BooleanField(default=False, verbose_name='是否在首页显示')),
            ],
        ),
    ]