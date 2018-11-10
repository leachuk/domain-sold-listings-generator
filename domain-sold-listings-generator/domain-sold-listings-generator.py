import psycopg2

conn = psycopg2.connect("dbname=property-dashboard-dev user=postgres")
cur = conn.cursor()

cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

my_string = "Hello, World!"
print(my_string)