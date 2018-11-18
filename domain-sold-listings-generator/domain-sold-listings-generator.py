import psycopg2

try:
    conn = psycopg2.connect("dbname=postgres user=postgres host=localhost")
except:
    print("Unable to connect to database")

cur = conn.cursor()

try:
    #cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    #cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
    #cur.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema'")
    cur.execute("SELECT postcode,place_name FROM public.au_postcodes WHERE state_code = 'VIC'")
except:
    print("failed to create table")

rows = cur.fetchall()

domain_sold_vic = []
for row in rows:
    #domain_sold_vic[row[0]] = "https://www.domain.com.au/sold-listings/?postcode={0}".format(row[0])
    domain_sold_vic.append({'postcode': row[0], 'placename': row[1], 'sold_listing_url': "https://www.domain.com.au/sold-listings/?postcode={0}".format(row[0])})
    #print("   postcode[{0}], name[{1}]".format(row[0], row[1]))

#print("domain_sold_vic 3000: {0}".format(domain_sold_vic['3000']))
print(domain_sold_vic[0])
print(domain_sold_vic[0]['sold_listing_url'])

#insert data into table
#cur.executemany("INSERT INTO public.domain_sold_urls(postcode,url) VALUES (%(first_name)s, %(last_name)s)", namedict)

# Make the changes to the database persistent and close communication with the database
conn.commit()
cur.close()
conn.close()
