# Generated by Django 4.0.3 on 2022-04-01 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_delete_counter_random_link_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='random_link',
            name='RL_number',
        ),
    ]