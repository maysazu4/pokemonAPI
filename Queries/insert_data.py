import json
import database
import random


def insert_single_type(connection, type_name):
    database.execute_query(connection,
        "INSERT INTO Type (name) VALUES (%s) ON DUPLICATE KEY UPDATE name=name",
        (type_name,)
    )
    return connection.cursor().lastrowid

def insert_pokemon(connection, pokemon, type_name):
    print(type_name)
    database.execute_query(connection,
        "INSERT IGNORE INTO pokemon (id, name, height, weight) VALUES (%s, %s, %s, %s)",
        (pokemon["id"], pokemon["name"], pokemon["height"], pokemon["weight"])
    )
    database.execute_query(connection,
        "INSERT IGNORE INTO pokemonType (pokemon_id, type_name) VALUES (%s, %s)",
        (pokemon["id"], type_name)
    )

# Load JSON data
with open('DB/pokemons_data.json') as file:
    data = json.load(file)

# Connect to MySQL database
connection = database.connect_to_database()

# Insert data into the pokemon table
    # Insert data into the pokemon table
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





# Insert data into the trainer table
trainers = set()
for pokemon in data:
    for trainer in pokemon["ownedBy"]:
        trainers.add((trainer["name"], trainer["town"]))

for trainer in trainers:
    database.execute_query(connection,
        "INSERT IGNORE INTO trainer (name, town) VALUES (%s, %s)",
        trainer
    )

# Insert data into the ownership table
for pokemon in data:
    for trainer in pokemon["ownedBy"]:
        if isinstance(pokemon["type"], list): 
            type_name = random.choice(pokemon["type"])
        else:
            type_name = pokemon["type"]

        database.execute_query(connection,
            "INSERT IGNORE INTO ownership (trainer_name, pokemon_id, type_name) VALUES (%s, %s, %s)",
            (trainer["name"], pokemon["id"], type_name)
        )

# Commit changes and close connection
database.close_connection(connection)
