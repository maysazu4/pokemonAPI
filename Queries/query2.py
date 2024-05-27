from Queries import database


def get_trainers_by_pokemon(name):
    # Connect to MySQL database
    connection = database.connect_to_database()

    query = """
    SELECT o.trainer_name
    FROM Ownership o
    JOIN Pokemon p ON p.id = o.pokemon_id
    WHERE p.name = %s;
    """

    # Execute the query with the parameter
    result = database.execute_and_fetch_query(connection,query, (name,))
    
    return result
    
 