#!/usr/bin/python3
"""
    Import libraries
"""
import sqlite3
from flask import Flask , render_template
from templates.routes_temp.index import index

app = Flask("Root")

@app.route('/')
def home():
    i = 0
    user = [[1,2,3,4],[2,2,3,4], [3] , [4]]
    # returning string
    return render_template("index.html", user=user)

@app.route('/MasterMind/<string:name>')
def log_inn(name):
    return index(name)


@app.route('/game')
def game():
    i = 0
    user = [[1,2,3,4],[2,2,3,4], [3] , [4]]
    # returning string
    return render_template("/html/game.html", user=user)

pages = ["/html/states.html", "/html/search.html"]

@app.route(pages[0])
def bar():
    # returning search bar
    return render_template(pages[0])

@app.route(pages[1])
def states():
    # returning states gallery
    return render_template(pages[1])

@app.route('/test')
def test():
    render_template('/test.py')

def err_pa():
    def get_db_connection():
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        return conn
    
    
    if __name__ == "__main__":        
        if get_db_connection() is False:
            render_template()


if __name__ == "__main__":
    app.run(debug=True, port=2427)
    
    con = err_pa()
    print(con)
