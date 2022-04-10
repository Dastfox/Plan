# Generated by Django 4.0.3 on 2022-04-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_random_link_rl_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='random_link',
            name='link',
        ),
        migrations.AlterField(
            model_name='random_link',
            name='RL_number',
            field=models.IntegerField(default=1),
        ),
    ]