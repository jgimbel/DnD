import psycopg2

#connect to the db
con = psycopg2.connect(
    host = 'localhost',
    database = 'dnd',
    user = 'postgres',
    password = 'postgres')
#cursor
cur = con.cursor()
cur.execute("SELECT unnest(enum_range(NULL::damage_types));")
damagetypes = []

#Create List of Damage Types
for n in cur:
    damagetypes.append(n[0])

#Go through each damage type and update the damage_types field to reflect the proper damage type
for n in damagetypes:
    cur.execute(f"UPDATE spells SET damage_type = '{n}' WHERE text LIKE '%__d__ {n} damage%' or text LIKE '%_d__ {n} damage%' or text LIKE '%__d_ {n} damage%' or text LIKE '%_d_ {n} damage%';")

#commit changes
con.commit()
#close the connection
con.close()