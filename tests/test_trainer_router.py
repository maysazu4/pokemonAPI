import pytest
from fastapi.testclient import TestClient
from pokemon_api.server import server



client=TestClient(server)

def test_get_trainers_by_pokemon_success():

    response = client.get("/trainer?pokemon_name=charmander")

    # Check response status code
    assert response.status_code == 200

    # Check response JSON content
    assert response.json() == ["Giovanni", "Jasmine", "Whitney"]


def test_get_trainers_by_pokemon_not_found():

#     # Send request to the endpoint
    response = client.get("/trainer?pokemon_name=NonExistentPokemon")
#
#     # Check response
    assert response.status_code == 404
    assert response.json() == {"detail": "No trainers found for the given Pokémon."}