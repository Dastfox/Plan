# Generated by Django 4.0.3 on 2022-04-01 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_counter_remove_random_link_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counter',
            old_name='number',
            new_name='Cnumber',
        ),
    ]
