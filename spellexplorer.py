import psycopg2
import sys
from psycopg2.extras import DictCursor

spellname = str(sys.argv[1])

#connect to the db
conn = psycopg2.connect(
    host = 'localhost',
    database = 'dnd',
    user = 'postgres',
    password = 'postgres')

#cursor
cur = conn.cursor(cursor_factory=DictCursor)

#SQL
test = cur.execute("SELECT * FROM spells WHERE spells.name ilike '%%'||%(spells)s||'%%';",{'spells': spellname})
rows = cur.fetchall()
if len(rows) > 1:
    for row in rows: 
        print(f"{row['name']}\n{', '.join(row['classes'])}\n")
else:
    for row in rows:
        print(f"\nName : {row['name']}\n\nClasses : {row['classes']}\n\nCasting Time: {row['time']}\nComponents : {row['components']}\nDuration : {row['duration']}\nLevel : {row['level']}\nMaterial : {row['material']}\nRange : {row['range']}\nRitual : {row['ritual']}\nSchool : {row['school']}\n\n{row['text']}\n\nSource : {row['source']}\nPage : {row['source_page']}\n")


#close the connection
conn.close()

