from fastapi import APIRouter, Query, HTTPException, Request
from Queries import query1, query2, query3, query_delete_pokemon, query_insert_pokemon
from pokemon_api.utils_get_info_http.get_pokemon_info import http_request_data, get_pokemon_info

router = APIRouter()


@router.get("/pokemon")
def get_pokemons(type: str = Query(None), trainer_name: str = Query(None)):
    if type and trainer_name:
        raise HTTPException(status_code=400, detail="Specify either type or trainer_name, not both.")
    elif type:
        return query1.get_pokemons_of_type(type)
    elif trainer_name:
        return query3.get_pokemons_by_trainer(trainer_name)
    else:
        raise HTTPException(status_code=400, detail="Specify at least one query parameter: type or trainer_name.")


@router.delete("/pokemon")
def delete_pokemon_of_trainer(trainer_name: str, pokemon_name: str):
    query_delete_pokemon.delete_pokemon_of_trainer(trainer_name, pokemon_name)
    return True


@router.post("/pokemon")
def add_pokemon(pokemon_name: str):
    response = http_request_data(pokemon_name)
    response.raise_for_status()
    data = response.json()
    pokemon_info = get_pokemon_info(data)
    query_insert_pokemon.insert_pokemon(pokemon_info)
    return True