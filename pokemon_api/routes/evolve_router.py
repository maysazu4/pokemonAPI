from fastapi import APIRouter,HTTPException
from Queries import query_exist
from Queries import query_delete_pokemon as d
from Queries import query_insert_pokemon_to_trainer as i
from Queries import query_insert_pokemon as p
from pokemon_api.utils import get_pokemon_info_utils as g
from pokemon_api.utils import evolve_utils as u

router = APIRouter()




@router.patch("/trainers/{trainer_name}/pokemons/{pokemon_name}")
async def evolve_pokemon(trainer_name:str, pokemon_name:str):
    if not query_exist.trainer_has_pokemon(trainer_name, pokemon_name):
        return f"{trainer_name} does not have {pokemon_name} pokemon"
    
    evolved_pokemon_name = await u.get_evolved_pokemon(pokemon_name)
    if not evolved_pokemon_name:
        raise HTTPException(status_code=404, detail=f"{pokemon_name} does not evolve")
    # Check if the evolved Pokémon exists in the trainer pokemons
    if query_exist.trainer_has_pokemon(trainer_name, evolved_pokemon_name):
        return f"{trainer_name} already has {evolved_pokemon_name} pokemon"
    # delete the old pokemon of the trainer 
    d.delete_pokemon_of_trainer(trainer_name,pokemon_name)
    # Add the evolved pokemon to the trainer
    i.insert_into_ownership(evolved_pokemon_name, trainer_name)
    # if the new pokemon not in the pokemon table  
    if not query_exist.pokemon_exists(evolved_pokemon_name):
        # add it
        pokemon_info = g.get_pokemon_info(pokemon_name)
        p.insert_pokemon(pokemon_info)
    
    return {"message": f"Evolved {pokemon_name} to {evolved_pokemon_name} for trainer {trainer_name}"}


