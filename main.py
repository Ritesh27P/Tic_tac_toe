from flask import Flask, render_template


app = Flask(__name__)
lobby = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


@app.route("/")
def home():
    global lobby
    print(lobby)
    return render_template('index.html', lobby=lobby)


@app.route("/tic_tac")
def tic_tac():
    pass


if __name__ == "__main__":
    app.run(debug=True)
