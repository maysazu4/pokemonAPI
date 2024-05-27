from fastapi import APIRouter

from Queries import query1, query2, query3

router = APIRouter()


@router.get("/pokemon/type/{type}")
def get_pokemons_by_type(type: str):
    return query1.get_pokemons_of_type(type)


@router.get("/pokemon/{pokemon_name}/trainers")
def get_trainers_by_pokemon(pokemon_name: str):
    print(pokemon_name)
    return query2.get_trainers_by_pokemon(pokemon_name)


@router.get("/trainer/{trainer_name}/pokemon")
def get_pokemons_by_trainer(trainer_name: str):
    return query3.get_pokemons_by_trainer(trainer_name)
