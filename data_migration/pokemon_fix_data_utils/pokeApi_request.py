import requests

base_url = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_types(pokemon_name):
    """
    Get the types of a specified Pokémon from the PokéAPI.

    Parameters:
    pokemon_name (str): The name of the Pokémon.

    Returns:
    list: A list of types for the specified Pokémon. If the request fails, an exception is raised.
    """

    response = requests.get(f"{base_url}{pokemon_name.lower()}")

    # Raise an HTTPError if the request returned an unsuccessful status code
    response.raise_for_status()

    data = response.json()
    types = [type_info["type"]["name"] for type_info in data["types"]]
    return types
