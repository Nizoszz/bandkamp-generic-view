# Generated by Django 4.0.7 on 2023-04-22 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ('id',)},
        ),
    ]
