# Generated by Django 4.1.2 on 2022-10-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_musicdata_lyric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicdata',
            name='lyric',
            field=models.CharField(default='', max_length=254),
        ),
    ]
