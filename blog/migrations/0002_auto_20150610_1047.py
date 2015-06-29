# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('author', models.CharField(max_length=200)),
                ('text', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='blog.Post'),
        ),
    ]
