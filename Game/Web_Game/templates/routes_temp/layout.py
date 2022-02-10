#!/usr/bin/python3


from templates.routes_temp.header import header
from templates.routes_temp.land_page import land_page

from templates.routes_temp.site_codes.Err_404 import Err_404

from templates.routes_temp.about_us import about_uss
from templates.routes_temp.MasterMind_Game import MasterMind_Game


from templates.routes_temp.footer import foot

def head():
    headd = '''
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                 <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                <link rel="icon" type="image/png" href="/static/assets/images/MasterMind_Game_Logo.png">
                <link rel="stylesheet" type="text/css" href="/static/css/styles.css"/>
                <title>MasterMind Game</title>
            </head>
    '''
    return headd

def layout(name):
    html = f'''
        <!DOCTYPE html>
            <html lang="en">
            {head()}           
            <body>
            {header()}
            <br><br><br>  
        '''
    
    if name == 'home':
        html += land_page()
    elif name == 'about_us':
        html += about_uss()
    elif name == 'game':
        html += MasterMind_Game()
    else:
        html += Err_404()

    html += f'''
            {foot()}
            </body>
            <script type="text/javascript" src="/static/js/alert.js"></script>
            </html>
            '''
    return html