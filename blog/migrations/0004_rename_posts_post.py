# Generated by Django 4.2.3 on 2023-08-14 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_tickets_ticket'),
        ('blog', '0003_rename_vip_user_posts_vip_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
