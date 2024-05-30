from fastapi import APIRouter, Query, HTTPException, Request
from Queries import query1, query3, query_delete_pokemon
from pokemon_api.utils.get_pokemon_info_utils import  get_pokemon_info
from Queries import query_insert_pokemon

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



@router.patch("/pokemons/{pokemon_name}/trainers/{trainer_name}")
def delete_pokemon_of_trainer(trainer_name: str, pokemon_name: str):
    try:
        # Assuming query_delete_pokemon.delete_pokemon_of_trainer returns a boolean or raises an exception
        affected_rows  = query_delete_pokemon.delete_pokemon_of_trainer(trainer_name, pokemon_name)
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Pokemon or trainer not found")
        return {"message": "Pokemon deleted successfully"}
    except HTTPException as http_exc:
        # Reraise HTTP exceptions to be handled by FastAPI
        raise http_exc
    except Exception as e:
        # Log the exception details (e.g., using a logging library)
        # For demonstration, we just print the error
        print(f"Unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


@router.post("/pokemon")
def add_pokemon(pokemon_name: str):
    pokemon_info = get_pokemon_info(pokemon_name)
    query_insert_pokemon.insert_pokemon(pokemon_info)
    return True

# געכעיכי