import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from Queries import database

'''
Inserts a single type to the types table
'''
def insert_single_type(connection, type_name):
    database.execute_query(connection,
        "INSERT INTO Type (name) VALUES (%s) ON DUPLICATE KEY UPDATE name=name",
                           (type_name,)
                           )
    return connection.cursor().lastrowid
'''
Inserts single pokemon to the pokemen table and its type to the pokemenType table 
'''
def insert_pokemon(connection, pokemon, type_name):
    database.execute_query(connection,
        "INSERT IGNORE INTO pokemon (id, name, height, weight) VALUES (%s, %s, %s, %s)",
                           (pokemon["id"], pokemon["name"], pokemon["height"], pokemon["weight"])
                           )
    database.execute_query(connection,
        "INSERT IGNORE INTO pokemonType (pokemon_id, type_name) VALUES (%s, %s)",
                           (pokemon["id"], type_name)
                           )
'''
Insert data into the pokemon table
'''
def insert_into_pokemons_and_types(data, connection):
    for pokemon in data:
        # If type is a single string
        if isinstance(pokemon["type"], str):
            insert_single_type(connection, pokemon["type"])
            insert_pokemon(connection, pokemon, pokemon["type"])
        # If type is a list of strings
        elif isinstance(pokemon["type"], list):
            for type_name in pokemon["type"]:
                insert_single_type(connection, type_name)
                insert_pokemon(connection, pokemon, type_name)
'''
Insert data into the trainer table
'''
def insert_into_trainer(data, connection):
    trainers = set()
    for pokemon in data:
        for trainer in pokemon["ownedBy"]:
            trainers.add((trainer["name"], trainer["town"]))

    for trainer in trainers:
        database.execute_query(connection,
            "INSERT IGNORE INTO trainer (name, town) VALUES (%s, %s)",
                               trainer
                               )
'''
Insert data into the ownership table
'''
def insert_into_ownership(data, connection):
    for pokemon in data:
        for trainer in pokemon["ownedBy"]:
            database.execute_query(connection,
                "INSERT IGNORE INTO ownership (trainer_name, pokemon_id) VALUES (%s, %s)",
                                   (trainer["name"], pokemon["id"])
                                   )
'''
Inserts all the data in the json files to MySql database
'''
def insert_data():
    # Load JSON data
    with open('POKEMONS/pokemons_data.json') as file:
        data = json.load(file)

    # Connect to MySQL database
    connection = database.connect_to_database()

    insert_into_pokemons_and_types(data,connection)
    insert_into_trainer(data,connection)
    insert_into_ownership(data, connection)

    # Commit changes and close connection
    database.close_connection(connection)

insert_data()