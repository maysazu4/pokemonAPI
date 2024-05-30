from Queries import database
from pokemon_api.utils.get_pokemon_info_utils import  get_pokemon_info

def insert_into_ownership(pokemon_name, trainer_name):
    connection = database.connect_to_database()
    try:
        pokemon_info = get_pokemon_info(pokemon_name)
        print(pokemon_info)
        database.execute_query(connection,
                               "INSERT INTO ownership (trainer_name, pokemon_id) VALUES (%s, %s)",
                               (trainer_name, pokemon_info[0])
                               )
        connection.commit()
        return f"Successfully inserted {pokemon_name} for trainer {trainer_name}."
    except Exception as e:
        connection.rollback()
        return f"Failed to insert {pokemon_name} for trainer {trainer_name}: {str(e)}"
    finally:
        connection.close()
