# Generated by Django 4.2 on 2023-04-20 15:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0003_goalcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalcomment',
            name='text',
            field=models.TextField(max_length=255, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='goalcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]