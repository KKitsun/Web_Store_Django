# Generated by Django 4.2.1 on 2023-05-26 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silvermoon', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='feature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='silvermoon.feature'),
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='silvermoon.genre'),
        ),
        migrations.AlterField(
            model_name='game',
            name='playersType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='silvermoon.playerstype'),
        ),
        migrations.AlterField(
            model_name='game',
            name='subgenre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='silvermoon.subgenre'),
        ),
        migrations.AlterField(
            model_name='game',
            name='theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='silvermoon.theme'),
        ),
        migrations.AlterField(
            model_name='game',
            name='visual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='silvermoon.visual'),
        ),
    ]