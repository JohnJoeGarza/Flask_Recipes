# -*- coding: utf-8 -*-
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
    
#Creation of the application instance
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE= os.path.join(app.root_path, 'flask_recipes.db'),
    SECRET_KEY = 'development key',
    USERNAME ='admin',
    PASSWORD = '0000'
        ))

app.config.from_envvar('FLASK_RECIPES_SETTINGS', silent=True)

def connect_db():
    '''Connects to the database specified.'''
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    ''' Opens a new database connection if there is none yet for the current 
    application context.
    '''
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
        
@app.teardown_appcontext
def close_db(error):
    '''Closes the database again at the end of the request'''
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('recipe_db_schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    
@app.cli.command('initdb')
def initdb_command():
    '''Initializes the database.'''
    init_db()
    print('Initialized the database.')

@app.route('/')
def show_recipes():
    db = get_db()
    cur = db.execute('select recipe_name, recipe_description from recipes order by id desc')
    recipes = cur.fetchall()
    return render_template('show_recipes.html', recipes=recipes)

@app.route('/addrecipe', methods=['POST'])
def add_recipe():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('\
               insert into recipes (recipe_name, recipe_description) \
               values(?,?)',
                [request.form['recipe_name'], request.form['recipe_description']]
                )
    db.commit()
    flash('New recipe has been posted')
    return redirect(url_for('show_recipes'))
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid Username/Password'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Username/Password'
        else:
            session['logged_in'] = True
            flash('Log In Successful')
            return redirect(url_for('show_recipes'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Log Out Successful')
    return redirect(url_for('show_recipes'))
    
    
    
    
    
    
    
    