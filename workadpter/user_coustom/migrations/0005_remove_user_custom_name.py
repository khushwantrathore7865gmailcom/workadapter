# Generated by Django 3.2.4 on 2021-06-17 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_coustom', '0004_remove_user_custom_confirmpass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_custom',
            name='name',
        ),
    ]