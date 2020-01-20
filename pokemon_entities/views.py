import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = PokemonEntity.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        add_pokemon(
            folium_map, pokemon.latitude, pokemon.longitude,
            pokemon.pokemon.title_ru, request.build_absolute_uri(pokemon.pokemon.image.url))

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title_ru,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon_descriptions = {
        'title_ru': pokemon.title_ru,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'img_url': pokemon.image.url,
        'description': pokemon.description,
    }

    if pokemon.evolution is not None:
        pokemon_descriptions['previous_evolution'] = {
                'title_ru': pokemon.evolution,
                'pokemon_id': pokemon.evolution.id,
                'img_url': pokemon.evolution.image.url,
            }

    next_evolution_pokemon = pokemon.evolutions_pokemon.first()
    if next_evolution_pokemon is not None:
        pokemon_descriptions['next_evolution'] = {
            'title_ru': next_evolution_pokemon.title_ru,
            'pokemon_id': next_evolution_pokemon.id,
            'img_url': next_evolution_pokemon.image.url,
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons = pokemon.pokemons_information.all()
    for pokemon in pokemons:
        add_pokemon(
            folium_map, pokemon.latitude, pokemon.longitude,
            pokemon.pokemon.title_ru, request.build_absolute_uri(pokemon.pokemon.image.url))

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon_descriptions, })
