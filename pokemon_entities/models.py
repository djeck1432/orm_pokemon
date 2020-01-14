from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField('названия покемона на русском', max_length=200)
    title_en = models.CharField('названия покемона на английском', max_length=200, null=True)
    title_jp = models.CharField('названия покемона на японском', max_length=200, null=True)
    image = models.ImageField('изображения покемона', null=True)
    description = models.TextField('описания к покемону', null=True)
    evolution = models.ForeignKey('self', verbose_name='эволюция  покемонов', related_name='pokemon_evolution',
                                  null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='названия покемона на русском', null=True,
                                on_delete=models.CASCADE)
    latitude = models.FloatField('широта')
    longitude = models.FloatField('долгота')
    appeared_at = models.DateTimeField('время появления', auto_now=False, null=True, blank=True)
    disappeared_at = models.DateTimeField('время исчезновения', auto_now=False, null=True, blank=True)
    level = models.IntegerField('уровень', null=True, blank=True)
    health = models.IntegerField('здоровья', null=True, blank=True)
    strength = models.IntegerField('сила', null=True, blank=True)
    defence = models.IntegerField('защита', null=True, blank=True)
    stamina = models.IntegerField('выносливость', null=True, blank=True)

    def __str__(self):
        return self.pokemon.title_ru
