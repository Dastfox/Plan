# Generated by Django 4.0.3 on 2022-04-01 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_remove_random_link_counter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='random_link',
            old_name='id',
            new_name='Counter',
        ),
    ]