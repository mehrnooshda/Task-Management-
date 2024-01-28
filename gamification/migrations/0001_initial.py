# Generated by Django 5.0.1 on 2024-01-20 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=100000)),
                ('category', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('complexity', models.CharField(max_length=50)),
                ('deadline', models.DateTimeField()),
            ],
        ),
    ]