# Generated by Django 4.0.7 on 2022-10-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletterApp', '0003_alter_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_important',
            field=models.BooleanField(default=False, verbose_name='importante'),
        ),
    ]
