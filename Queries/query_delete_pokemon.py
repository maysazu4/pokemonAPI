from Queries import database


def delete_pokemon_of_trainer(trainer_name,pokemon_name):
    connection = database.connect_to_database()
    query = """
    DELETE FROM Ownership 
    WHERE pokemon_id = (SELECT id FROM pokemon WHERE name = %s )
    AND trainer_name = %s ;
    """
    database.execute_query(connection, query, (pokemon_name,trainer_name,))
    



