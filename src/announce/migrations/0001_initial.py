# Generated by Django 4.2.1 on 2023-05-09 20:03

import announce.models
import autoslug.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='제목')),
                ('body', models.TextField(max_length=2000, verbose_name='내용')),
                ('image', models.ImageField(blank=True, null=True, upload_to=announce.models.upload_location, verbose_name='사진')),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='업로드 일짜')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='마지막 업데이트')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True, validators=[django.core.validators.RegexValidator('^[가-힣A-Za-z0-9_-]+$', 'Only Korean letters, alphanumeric, hyphen, and underscore characters are allowed.')])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announce_blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name': '공지사항',
                'verbose_name_plural': '공지사항',
            },
        ),
    ]
