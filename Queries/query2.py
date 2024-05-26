# import Queries.create_tables as t



# # Insert a record
# t.cursor.execute('''
# INSERT INTO Pokemon (id,name,type,height,weight) VALUES (%s,%s,%s,%s,%s)
# ''', ( 1,"bulbasaur","grass",7,69)
# )

# # Commit the changes
# t.conn.commit()

# # Query the database
# t.cursor.execute('SELECT * FROM Pokemon')
# rows = t.cursor.fetchall()
# for row in rows:
#     print(row)

# # Close the connection
# t.conn.close()
