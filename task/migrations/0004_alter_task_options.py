# Generated by Django 4.0.6 on 2022-08-01 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_options_alter_task_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['done']},
        ),
    ]
