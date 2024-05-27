from fastapi import APIRouter

from Queries import delete_pokemon 

router = APIRouter()


@router.delete("/pokemon")
def delete_pokemon_of_trainer(trainer_name:str, pokemon_name:str):
    delete_pokemon.delete_pokemon_of_trainer(trainer_name,pokemon_name)
    return True




