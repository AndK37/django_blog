# Generated by Django 5.1.7 on 2025-03-21 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_commentrating_user_alter_comment_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentRating',
        ),
    ]
