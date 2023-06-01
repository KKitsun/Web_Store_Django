# Generated by Django 4.2.1 on 2023-05-26 17:19

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('silvermoon', '0002_remove_game_feature_remove_game_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('releaseDate', models.DateField()),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('description', models.TextField(max_length=5000)),
                ('developer', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('feature', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='silvermoon.feature')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('O', 'Ordered'), ('R', 'Ready'), ('C', 'Completed')], default='O', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='PlayersType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Subgenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Visual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='OrderGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silvermoon.game')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silvermoon.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='games',
            field=models.ManyToManyField(through='silvermoon.OrderGame', to='silvermoon.game'),
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='silvermoon.genre'),
        ),
        migrations.AddField(
            model_name='game',
            name='playersType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='silvermoon.playerstype'),
        ),
        migrations.AddField(
            model_name='game',
            name='subgenre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='silvermoon.subgenre'),
        ),
        migrations.AddField(
            model_name='game',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='silvermoon.theme'),
        ),
        migrations.AddField(
            model_name='game',
            name='visual',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='silvermoon.visual'),
        ),
    ]
