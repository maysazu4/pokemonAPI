from fastapi import APIRouter, Query

from Queries import query2, query_insert_pokemon_to_trainer

router = APIRouter()


@router.get("/trainer")
def get_trainers_by_pokemon(pokemon_name: str):
    return query2.get_trainers_by_pokemon(pokemon_name)


@router.post("/trainer")
def add_pokemon_to_trainer(trainer_name: str = Query(...), pokemon_id: int = Query(...)):

    print(pokemon_id)
    return query_insert_pokemon_to_trainer.insert_into_ownership(pokemon_id, trainer_name)
