# Generated by Django 4.0.3 on 2022-03-31 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_random_link_rl_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='random_link',
            name='RL_number',
            field=models.IntegerField(default=0),
        ),
    ]
