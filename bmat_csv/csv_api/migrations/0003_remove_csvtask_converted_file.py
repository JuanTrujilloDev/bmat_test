# Generated by Django 4.2 on 2023-04-26 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_api', '0002_alter_csvtask_options_remove_csvtask_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvtask',
            name='converted_file',
        ),
    ]