# Generated by Django 4.1.6 on 2023-02-22 08:17

import anarticle.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, help_text='Characters combine with numbers, underscores or hyphens.Ex: today1_news-headline')),
                ('summary', models.TextField()),
                ('image', models.ImageField(blank=True, help_text='Upload file should under size limitation, with png, jpg or jpeg file extensions.', upload_to=anarticle.utils.image_path)),
                ('is_published', models.BooleanField(default=True, help_text='Designates whether the item is published on the site.', verbose_name='Published')),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, help_text='Upload file should under size limitation, with png, jpg or jpeg file extensions.', upload_to=anarticle.utils.image_path)),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, help_text='Upload file should under size limitation, with png, jpg or jpeg file extensions.', upload_to=anarticle.utils.image_path)),
                ('image_text', models.CharField(blank=True, help_text='Descripe the image content', max_length=255)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anarticle.article')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, help_text='Upload file should under size limitation, with png, jpg or jpeg file extensions.', upload_to=anarticle.utils.image_path)),
                ('tags', models.ManyToManyField(to='anarticle.tag')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='anarticle.tag'),
        ),
    ]
