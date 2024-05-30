import pytest
from fastapi.testclient import TestClient
from pokemon_api.routes import pokemon_router
from pokemon_api.server import server


# Create a TestClient
client = TestClient(server)

# Define test cases
def test_get_pokemons_type():
    response = client.get("/pokemon?type=fire")
    assert response.status_code == 200
    assert response.json() == ["charmander","charmeleon","charizard","vulpix","ninetales","growlithe","arcanine","ponyta","rapidash","magmar","flareon","moltres"]

def test_get_pokemons_trainer_name():
    response = client.get("/pokemon?trainer_name=Giovanni")
    assert response.status_code == 200
    assert response.json() == ["bulbasaur","venusaur","charmander","wartortle","caterpie","beedrill","oddish","parasect","primeape","weepinbell","eevee"]

def test_get_pokemons_both_params():
    
    response = client.get("/pokemon?type=Electric&trainer_name=Ash")
    assert response.status_code == 400
    assert response.json() == {"detail": "Specify either type or trainer_name, not both."}

def test_get_pokemons_no_params():
    response = client.get("/pokemon")
    assert response.status_code == 400
    assert response.json() == {"detail": "Specify at least one query parameter: type or trainer_name."}
