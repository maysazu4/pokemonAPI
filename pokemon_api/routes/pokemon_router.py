from fastapi import APIRouter, Query, HTTPException, Request
from Queries import query1, query3, query_delete_pokemon,query_exist
from pokemon_api.utils.get_pokemon_info_utils import get_pokemon_info
from Queries import query_insert_pokemon

router = APIRouter()


@router.get("/pokemon")
def get_pokemons(type: str = Query(None), trainer_name: str = Query(None)):
    if type and trainer_name:
        raise HTTPException(status_code=400, detail="Specify either type or trainer_name, not both.")
    elif type:
        if not query_exist.type_exists(type):
            raise HTTPException(status_code=404, detail=f"{type} type not found.")
        pokemons = query1.get_pokemons_of_type(type)
        if not pokemons:
            raise HTTPException(status_code=404, detail=f"No pokemons found of type {type}.")
        return pokemons
    elif trainer_name:
        if not query_exist.trainer_exists(trainer_name):
            raise HTTPException(status_code=404, detail=f"{trainer_name} trainer not found.")
        pokemons = query3.get_pokemons_by_trainer(trainer_name)
        if not pokemons:
            raise HTTPException(status_code=404, detail=f"No pokemons found for trainer {trainer_name}.")
        return pokemons
    else:
        raise HTTPException(status_code=400, detail="Specify at least one query parameter: type or trainer_name.")


@router.patch("/pokemons/{pokemon_name}/trainers/{trainer_name}")
def delete_pokemon_of_trainer(trainer_name: str, pokemon_name: str):
        if not query_exist.pokemon_exists(pokemon_name):
            raise HTTPException(status_code=404, detail=f"{pokemon_name} pokemon not found.")
        if not query_exist.trainer_exists(trainer_name):
            raise HTTPException(status_code=404, detail=f"{trainer_name} trainer not found.")
        if not query_exist.trainer_has_pokemon(trainer_name, pokemon_name):
            raise HTTPException(status_code=404, detail=f"{trainer_name} does not have {pokemon_name} pokemon")
        query_delete_pokemon.delete_pokemon_of_trainer(trainer_name, pokemon_name)
        return {"message": "Pokemon deleted successfully"}

@router.post("/pokemon")
def add_pokemon(pokemon_name: str):
    if query_exist.pokemon_exists(pokemon_name):
        raise HTTPException(status_code=409, detail=f"{pokemon_name} pokemon is already in the database.")
    pokemon_info = get_pokemon_info(pokemon_name)
    query_insert_pokemon.insert_pokemon(pokemon_info)
    return {"message": "Pokemon added successfully"}
