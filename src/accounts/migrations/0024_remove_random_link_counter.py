# Generated by Django 4.0.3 on 2022-04-01 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_random_link_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='random_link',
            name='Counter',
        ),
    ]