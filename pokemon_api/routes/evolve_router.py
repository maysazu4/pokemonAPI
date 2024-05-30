from fastapi import APIRouter, HTTPException
from Queries import query_exist
from Queries.query_delete_pokemon import delete_pokemon_of_trainer
from Queries.query_insert_pokemon import insert_pokemon
from Queries.query_insert_pokemon_to_trainer import insert_into_ownership
from pokemon_api.utils.evolve_utils import get_evolved_pokemon
from pokemon_api.utils.get_pokemon_info_utils import get_pokemon_info

router = APIRouter()


@router.patch("/trainers/{trainer_name}/pokemons/{pokemon_name}")
async def evolve_pokemon(trainer_name: str, pokemon_name: str):
    if not query_exist.trainer_has_pokemon(trainer_name, pokemon_name):
        raise HTTPException(status_code=404, detail=f"{trainer_name} does not have {pokemon_name} pokemon")

    evolved_pokemon_name = await get_evolved_pokemon(pokemon_name)
    if not evolved_pokemon_name:
        raise HTTPException(status_code=400, detail=f"{pokemon_name} does not evolve")

    if query_exist.trainer_has_pokemon(trainer_name, evolved_pokemon_name):
        raise HTTPException(status_code=409, detail=f"{trainer_name} already has {evolved_pokemon_name} pokemon")

    delete_pokemon_of_trainer(trainer_name, pokemon_name)

    insert_into_ownership(evolved_pokemon_name, trainer_name)

    if not query_exist.pokemon_exists(evolved_pokemon_name):
        pokemon_info = get_pokemon_info(pokemon_name)
        insert_pokemon(pokemon_info)

    return {"message": f"Evolved {pokemon_name} to {evolved_pokemon_name} for trainer {trainer_name}"}
