# Generated by Django 3.2 on 2021-10-21 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('url', models.CharField(max_length=1000)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
