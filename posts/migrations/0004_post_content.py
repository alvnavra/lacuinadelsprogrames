# Generated by Django 2.2.4 on 2019-08-06 21:56

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default=True),
            preserve_default=False,
        ),
    ]
