import json
import psycopg2

with open('/Users/benholloway/Documents/DnDPnP/spells.json') as f:
    data = json.load(f)

#connect to the db
con = psycopg2.connect(
    host = 'localhost',
    database = 'dnd',
    user = 'postgres',
    password = 'postgres')

#cursor
cur = con.cursor()

print('PostgreSQL database version:')
print(cur.execute('SELECT version();'))

for n in data:    
    nameN = n
    classesN = data[n]['classes']
    componentsN = data[n]['components']
    durationN = data[n]['duration']
    levelN = data[n]['level']
    materialN = data[n]['material']
    rangeN = data[n]['range']
    ritualN = data[n]['ritual']
    schoolN = data[n]['school']
    sourceN = data[n]['source']
    source_pageN = data[n]['source_page']
    textN = data[n]['text']
    timeN = data[n]['time']
    print('INSERT INTO spells (name, classes, components, duration, level, material, range, ritual, school, source, source_page, text, time) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (nameN, classesN, componentsN, durationN, levelN, materialN, rangeN, ritualN, schoolN, sourceN, source_pageN, textN, timeN)) 
    print('\n')
    cur.execute(
    "INSERT INTO spells (name, classes, components, duration, level, material, range, ritual, school, source, source_page, text, time) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nameN, classesN, componentsN, durationN, levelN, materialN, rangeN, ritualN, schoolN, sourceN, source_pageN, textN, timeN))  

#close the conneciton
con.commit()
con.close()
