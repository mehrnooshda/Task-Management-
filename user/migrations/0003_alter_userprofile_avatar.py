# Generated by Django 5.0.1 on 2024-01-24 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userprofile_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.avatar'),
        ),
    ]
