# Generated by Django 4.0.3 on 2022-04-01 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_random_link_rl_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='random_link',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]