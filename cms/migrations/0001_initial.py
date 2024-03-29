# Generated by Django 4.1.3 on 2023-01-21 20:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('intro', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('blog_date', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='blog')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('blog', models.ManyToManyField(to='cms.blog')),
            ],
        ),
    ]
