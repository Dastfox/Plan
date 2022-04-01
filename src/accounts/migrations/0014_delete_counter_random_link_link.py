# Generated by Django 4.0.3 on 2022-04-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_counter_cnumber'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Counter',
        ),
        migrations.AddField(
            model_name='random_link',
            name='link',
            field=models.URLField(default='https://fr.wikipedia.org/wiki/Julien_Lepers', max_length=2300),
            preserve_default=False,
        ),
    ]
