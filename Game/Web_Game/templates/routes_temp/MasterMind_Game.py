#!/usr/bin/python3
import random

colors = ['red', 'blue', 'white', 'brown', 'yellow', 'black']  

def color_code(color):
    game = '''
            <div>
    '''
    game += f'''
            <div
                    style="width: 23px;
                    background: {color};
                    border-radius: 60px;
                    margin-left: 10px;
                    height: 23px;"
                    >C
                    '''
    game += '''
                </div>
                <br>
            </div>
        '''
    return game

def table():
    fila = 0
    columna = 0
    count = 0 
    count2 = 0
    my_tabla = [
                [ 'X', 'X', 'X', 'X','X', 'X', 'X', 'X'],
                [ 'X', 'X', 'X', 'X','X', 'X', 'X', 'X'],
                [ 'X', 'X', 'X', 'X','X', 'X', 'X', 'X'],
                [ 'X', 'X', 'X', 'X','X', 'X', 'X', 'X'],
                ]
    game = ' <div style="display:flex; text-align:center;">'
                
    for fila in my_tabla:
        game += '''
                <div 
                    style="width: 22px;
                    border-radius: 60px;
                    margin-left: 10px;"
                    >'''
        
        #if count == 4:
         #   game += '''
          #      <br>
           #     '''
            #count = 0

        #count += 1
        for columna in fila:
            game += '''
                        <div 
                            style="width: 22px;
                            background: rosybrown;
                            border-radius: 60px;
                            margin-left: 10px;
                            text-align:left;"
                            >Y</div>
                        '''
            if count2 == 4:
                game += '''
            
                '''
                count2 = 0
            count2+=1
        
        game += '''</div>'''
                    
    game += '''
            </div>
            '''
    return game


def init_game():
    new_code = []
    code_user = []
      
    game = ''''''

    for i in range(4):
        new_code.append(random.choice(colors))

    for color in new_code:
       game += color_code(color)

    game += table()
    return game

def MasterMind_Game():
    Game = f'''
        <div">
            <a>Iniciando el Juego</a>
            <div style="display:flex;">
                {init_game()}
            </div>
        </div>
    '''

    return Game


if __name__ == "__main__":
    MasterMind_Game()