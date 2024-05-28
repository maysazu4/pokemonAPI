from Queries import database
from pokemon_api.utils.get_pokemon_info_utils import  get_pokemon_info


def insert_into_ownership(pokemon_name, trainer_name):
    connection = database.connect_to_database()
    pokemon_info = get_pokemon_info(pokemon_name)
    database.execute_query(connection,
                           "INSERT ownership (trainer_name, pokemon_id) VALUES (%s, %s)",
                           (trainer_name, pokemon_info[0])
                           )
