import psycopg2
from psycopg2 import OperationalError

try:
    # Connect to PostgreSQL
    connection = psycopg2.connect(
        dbname="chinook",
        user="postgres",
        password="waggies1",
        host="localhost",
        port="5432"
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute the query
    # cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

    # Query 2 - select only the "Name" column from the "Artist" table
    # cursor.execute('SELECT "name" FROM "artist"')
    
    # Query 3 - select only "Queen" from the "Artist" table
    #cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])
    # Fetch the results
    
    # Query 4 - select only by "ArtistId" #51 from the "Artist" table
    # cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51])
    
    # Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
    # cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])
    
    # Query 6 - select all tracks where the composer is "Queen" from the "Track" table
    cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

    
    results = cursor.fetchall()
    # fetch the result (single)
    #results = cursor.fetchone()

    # Print results
    for result in results:
        print(result)

except OperationalError as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
