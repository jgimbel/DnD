from flask import Flask, url_for, render_template
import psycopg2
from psycopg2.extras import RealDictCursor, DictCursor

app = Flask(__name__)

con = psycopg2.connect(
    host = 'localhost',
    database = 'dnd',
    user = 'postgres',
    password = 'postgres')
@app.route('/')
def spells():

    #cursor
    with con.cursor(cursor_factory=DictCursor) as cur:
        cur.execute('select id, name from spells;')
        spells = [x for x in cur]
        print(spells)
        return render_template('spells.html', spells=spells)

@app.route('/<spell_id>')
def spell(spell_id):
    #cursor
    with con.cursor(cursor_factory=DictCursor) as cur:
        cur.execute('select * from spells where id = %s::int;', (spell_id, ))
        response = [x for x in cur]
        if(len(response) < 1):
            return 'No spell found'
        print(response[0])
        return render_template('spell.html', spell=response[0])
