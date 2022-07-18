from flask import Flask, render_template, redirect, url_for, request
import numpy as np

app = Flask(__name__)
starting_symbol = True
lobby = np.array([[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']])

# todo making a comination
x_win = 0
y_win = 0
combination = []
for a in range(3):
    for b in range(3):
        combination.append((a, b))
win_combination = [[combination[:3]], [combination[3:6]], [combination[6:9]], [combination[:9:3]], [combination[:9:3]], [combination[1:9:3]],
                   [combination[2:9:3]], [[(0, 0), (1, 1), (2, 2)]], [[(0, 2), (1, 1), (2, 0)]]]


@app.route("/")
def home():
    global lobby
    return render_template('index.html', lobby=lobby)


@app.route("/tic_tac/", methods=["POST", 'GET'])
def tic_tac():
    if request.method == 'POST':
        global starting_symbol, win_combination, lobby, x_win, y_win
        temp = request.form.get('b1')
        i, j = temp.split(" ")
        i, j = int(i), int(j)
        if starting_symbol and (lobby[i][j] == ' '):
            lobby[i][j] = "X"
            starting_symbol = False
        elif not starting_symbol and (lobby[i][j] == ' '):
            print('hii')
            lobby[i][j] = 'O'
            starting_symbol = True

        for i in lobby:
            if ' ' in i:
                break
            else:
                return redirect(url_for('home', win=None))


        temp = ''
        for i in win_combination:
            for j in i:
                for k in j:
                    a, b = k[0], k[1]
                    if lobby[a][b] == 'O' or 'X':
                        temp += lobby[a][b]
                if temp == 'XXX':
                    x_win += 1
                    lobby = np.array([[' ', ' ', ' '],
                                      [' ', ' ', ' '],
                                      [' ', ' ', ' ']])
                    return render_template('index.html', win='X', lobby=lobby, x=x_win, y=y_win)
                if temp == 'OOO':
                    y_win += 1
                    lobby = np.array([[' ', ' ', ' '],
                                      [' ', ' ', ' '],
                                      [' ', ' ', ' ']])
                    return render_template('index.html', win='O', lobby=lobby, x=x_win, y=y_win)
                temp = ''
    return redirect(url_for('home', win=None))


if __name__ == "__main__":
    app.run(debug=True)
    pass





