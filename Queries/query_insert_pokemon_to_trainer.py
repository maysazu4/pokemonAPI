from Queries import database


def insert_into_ownership(pokemon_id, trainer_name):
    connection = database.connect_to_database()

    database.execute_query(connection,
                           "INSERT ownership (trainer_name, pokemon_id) VALUES (%s, %s)",
                           (trainer_name, pokemon_id)
                           )
