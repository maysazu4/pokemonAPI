from Queries import database

def create_pokemon_table(connection):
    database.execute_query(connection,'''
    CREATE TABLE IF NOT EXISTS Pokemon (
        id INT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        height FLOAT NOT NULL,
        weight FLOAT NOT NULL
    )
    '''
    )

def create_type_table(connection):
    database.execute_query(connection,'''
    CREATE TABLE IF NOT EXISTS Type (
        name VARCHAR(255) PRIMARY KEY
    )
    ''')

def create_pokemon_type_table(connection):
    database.execute_query(connection,'''
    CREATE TABLE IF NOT EXISTS PokemonType (
        pokemon_id INT,
        type_name VARCHAR(255),
        PRIMARY KEY (pokemon_id, type_name),
        FOREIGN KEY (pokemon_id) REFERENCES Pokemon(id),
        FOREIGN KEY (type_name) REFERENCES Type(name)
    )
    ''')

def create_trainer_table(connection):
    database.execute_query(connection,'''
    CREATE TABLE IF NOT EXISTS Trainer (
        name VARCHAR(255) PRIMARY KEY,
        town VARCHAR(255) NOT NULL
    )
    ''')

def create_ownership_table(connection):
    database.execute_query(connection,'''
    CREATE TABLE IF NOT EXISTS Ownership (
        trainer_name VARCHAR(255),
        pokemon_id INT,
        PRIMARY KEY (trainer_name, pokemon_id),
        FOREIGN KEY (trainer_name) REFERENCES Trainer(name),
        FOREIGN KEY (pokemon_id) REFERENCES Pokemon(id) 
    )
    ''')

def create_tables():
    # Connect to the database
    connection = database.connect_to_database()
    create_pokemon_table(connection)
    create_trainer_table(connection)
    create_type_table(connection)
    create_ownership_table(connection)
    create_pokemon_type_table(connection)
    database.close_connection(connection)

create_tables()