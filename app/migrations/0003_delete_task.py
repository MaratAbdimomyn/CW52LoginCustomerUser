# Generated by Django 4.2.2 on 2023-11-16 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_task_alter_customer_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]