import database


def get_pokemons_of_type(type_name):
    connection = database.connect_to_database()
    query = """
    SELECT p.name FROM Pokemon p
    JOIN PokemonType pt ON pt.pokemon_id=p.id WHERE pt.type_name=%s;
    """
    result = database.execute_and_fetch_query(connection, query, (type_name,))
    return result


print(get_pokemons_of_type("grass"))
