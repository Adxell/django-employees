# Generated by Django 4.1.2 on 2022-10-07 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_remove_employee_user_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
