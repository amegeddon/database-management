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
    cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

    # Fetch the results
    results = cursor.fetchall()

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
