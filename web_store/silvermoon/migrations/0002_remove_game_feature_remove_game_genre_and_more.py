# Generated by Django 4.2.1 on 2023-05-26 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('silvermoon', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='game',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='game',
            name='playersType',
        ),
        migrations.RemoveField(
            model_name='game',
            name='subgenre',
        ),
        migrations.RemoveField(
            model_name='game',
            name='theme',
        ),
        migrations.RemoveField(
            model_name='game',
            name='visual',
        ),
        migrations.RemoveField(
            model_name='order',
            name='games',
        ),
        migrations.RemoveField(
            model_name='orderedgames',
            name='game',
        ),
        migrations.RemoveField(
            model_name='orderedgames',
            name='order',
        ),
        migrations.DeleteModel(
            name='Feature',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderedGames',
        ),
        migrations.DeleteModel(
            name='PlayersType',
        ),
        migrations.DeleteModel(
            name='Subgenre',
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
        migrations.DeleteModel(
            name='Visual',
        ),
    ]
