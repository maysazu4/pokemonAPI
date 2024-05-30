from Queries import database



def pokemon_exists(pokemon_name):
    connection = database.connect_to_database()
    query = """
    SELECT id 
    FROM Pokemon 
    WHERE name=%s;
    """
    result = database.execute_and_fetch_query(connection, query, (pokemon_name,))
    return len(result) != 0

def trainer_has_pokemon(trainer_name, pokemon_name):
    connection = database.connect_to_database()
    query = """
    SELECT p.name 
    FROM Pokemon p
    JOIN Ownership o ON o.pokemon_id=p.id 
    WHERE p.name=%s AND o.trainer_name = %s;
    """
    result = database.execute_and_fetch_query(connection, query, (pokemon_name, trainer_name))
    return len(result) != 0

def type_exists(type):
    connection = database.connect_to_database()
    query = """
    SELECT name 
    FROM Type 
    WHERE name=%s;
    """
    result = database.execute_and_fetch_query(connection, query, (type,))
    return len(result) != 0

def trainer_exists(trainer_name):
    connection = database.connect_to_database()
    query = """
    SELECT name 
    FROM Trainer 
    WHERE name=%s;
    """
    result = database.execute_and_fetch_query(connection, query, (trainer_name,))
    return len(result) != 0
