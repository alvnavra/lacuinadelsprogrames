# Generated by Django 2.2.4 on 2019-08-15 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20190814_2230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'verbose_name_plural': 'Llenguatges'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_last_posts',
            field=models.CharField(default='Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_newsletter',
            field=models.CharField(default='title', max_length=100),
        ),
    ]