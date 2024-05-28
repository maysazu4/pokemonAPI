from Queries import database


def get_pokemons_by_trainer(name):
    # Connect to MySQL database
    connection = database.connect_to_database()

    query = """
    SELECT p.name
    FROM Pokemon p
    JOIN Ownership o ON p.id = o.pokemon_id
    WHERE o.trainer_name = %s;
    """

    # Execute the query with the parameter
    result = database.execute_and_fetch_query(connection, query, (name,))
    
    return result
    
#fhgjh
