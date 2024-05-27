from Queries import database


def insert_pokemon(pokemon_info):
    connection = database.connect_to_database()
    database.execute_query(connection,
        "INSERT IGNORE INTO pokemon (id, name, height, weight) VALUES (%s, %s, %s, %s)",
                           (pokemon_info[0], pokemon_info[1], pokemon_info[2], pokemon_info[3])
                           )
    types = pokemon_info[4]
    for type_ in types:
        database.execute_query(connection,
            "INSERT IGNORE INTO pokemonType (pokemon_id, type_name) VALUES (%s, %s)",
                               (pokemon_info[0],type_)
                               )



