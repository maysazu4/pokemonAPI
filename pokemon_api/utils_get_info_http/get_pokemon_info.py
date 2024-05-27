import requests

base_url = "https://pokeapi.co/api/v2/pokemon/"


def http_request_data(pokemon_name):
    return requests.get(f"{base_url}{pokemon_name.lower()}")


def get_pokemon_info(data):
    types = []
    for d in data["types"]:
        types.append(d["type"]["name"])

    return [data["id"], data["species"]["name"], data["height"], data["weight"], types]
