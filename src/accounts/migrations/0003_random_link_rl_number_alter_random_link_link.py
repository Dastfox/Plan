# Generated by Django 4.0.3 on 2022-03-31 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_random_link_delete_operateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='random_link',
            name='RL_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='random_link',
            name='link',
            field=models.URLField(max_length=2300),
        ),
    ]
