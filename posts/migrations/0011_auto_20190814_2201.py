# Generated by Django 2.2.4 on 2019-08-14 20:01

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_remove_post_titulo2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llenguatge', models.CharField(choices=[('EN', 'Anglès'), ('ES', 'Espanyol'), ('CA', 'Català')], default='CA', max_length=10)),
            ],
            options={
                'verbose_name': 'Lllenguatge',
                'verbose_name_plural': 'Llenguatges',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('overview', models.CharField(max_length=25)),
                ('title_last_posts', models.CharField(max_length=25)),
                ('description_last_posts', models.CharField(max_length=100)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Author')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Language')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.Blog'),
        ),
    ]
