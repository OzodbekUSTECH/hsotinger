# Generated by Django 4.2.1 on 2023-06-03 11:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_blog_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
    ]
