# Generated by Django 2.2.3 on 2020-01-13 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_pokemon_evolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon'),
        ),
    ]
