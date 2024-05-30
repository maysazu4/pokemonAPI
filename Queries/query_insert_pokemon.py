from Queries import database

def insert_pokemon(pokemon_info):
    connection = database.connect_to_database()
    try:
        # Start a transaction
        cursor = connection.cursor()

        # Insert into pokemon table
        cursor.execute(
            "INSERT IGNORE INTO pokemon (id, name, height, weight) VALUES (%s, %s, %s, %s)",
            (pokemon_info[0], pokemon_info[1], pokemon_info[2], pokemon_info[3])
        )

        # Insert into pokemonType table
        types = pokemon_info[4]
        for type_ in types:
            cursor.execute(
                "INSERT IGNORE INTO pokemonType (pokemon_id, type_name) VALUES (%s, %s)",
                (pokemon_info[0], type_)
            )

        # Commit the transaction
        connection.commit()
        return f"Successfully inserted Pokémon '{pokemon_info[1]}' with ID '{pokemon_info[0]}'."
    except Exception as e:
        connection.rollback()
        return f"Failed to insert Pokémon '{pokemon_info[1]}' with ID '{pokemon_info[0]}': {str(e)}"
    finally:
        connection.close()
