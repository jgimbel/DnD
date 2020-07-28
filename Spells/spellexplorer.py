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
cur.execute("SELECT * FROM spells WHERE spells.name = %(spells)s;",{'spells': spellname})
match = cur.fetchall()
if len(match) == 1:
     print(f"\nName : {match[0]['name']}\n\nClasses : {match[0]['classes']}\n\nCasting Time: {match[0]['time']}\nComponents : {match[0]['components']}\nDuration : {match[0]['duration']}\nLevel : {match[0]['level']}\nMaterial : {match[0]['material']}\nRange : {match[0]['range']}\nRitual : {match[0]['ritual']}\nSchool : {match[0]['school']}\n\n{match[0]['text']}\n\nSource : {match[0]['source']}\nPage : {match[0]['source_page']}\n")
else: 
    cur.execute("SELECT * FROM spells WHERE spells.name ilike '%%'||%(spells)s||'%%';",{'spells': spellname})
    rows = cur.fetchall()
    if len(rows) > 1:
     for row in rows: 
            print(f"{row['name']}\n{', '.join(row['classes'])}\n")
    else:
        for row in rows:
          print(f"\nName : {row['name']}\n\nClasses : {row['classes']}\n\nCasting Time: {row['time']}\nComponents : {row['components']}\nDuration : {row['duration']}\nLevel : {row['level']}\nMaterial : {row['material']}\nRange : {row['range']}\nRitual : {row['ritual']}\nSchool : {row['school']}\n\n{row['text']}\n\nSource : {row['source']}\nPage : {row['source_page']}\n")


#close the connection
conn.close()

