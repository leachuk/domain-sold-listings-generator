import psycopg2

try:
    conn = psycopg2.connect("dbname=postgres user=postgres host=localhost")
except:
    print("Unable to connect to database")

cur = conn.cursor()

try:
    #cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    #cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
    cur.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema'")
except:
    print("failed to create table")

rows = cur.fetchall()
print("\nRows: \n")
for row in rows:
    print("   ", row[1])

# Make the changes to the database persistent and close communication with the database
conn.commit()
cur.close()
conn.close()

my_string = "Hello, World!"
print(my_string)