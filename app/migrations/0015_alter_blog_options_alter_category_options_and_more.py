# Generated by Django 4.2.1 on 2023-05-17 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_multipleimage_delete_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='multipleimage',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения!'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='file',
            field=models.FileField(blank=True, upload_to='files/', verbose_name='Файл для скачивания(pdf)'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_uz',
            field=models.CharField(max_length=500, null=True, verbose_name='Название'),
        ),
    ]
