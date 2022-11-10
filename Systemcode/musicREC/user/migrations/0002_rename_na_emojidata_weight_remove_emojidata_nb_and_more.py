# Generated by Django 4.1.2 on 2022-10-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emojidata',
            old_name='NA',
            new_name='weight',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='NB',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='NC',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='ND',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='NE',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='NG',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='NH',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='NI',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='NJ',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='NK',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='NL',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='NN',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='PA',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='PB',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='PC',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='PD',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='PE',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='PF',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='PG',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='PH',
        ),
        migrations.RemoveField(
            model_name='emojidata',
            name='PK',
        ),
        migrations.AddField(
            model_name='emojidata',
            name='emoji',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
