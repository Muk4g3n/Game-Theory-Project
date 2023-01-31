from flask import Flask,request
from game import Game


app = Flask(__name__)

gameRound = Game()

@app.route('/play',methods = ['POST','GET'])
def index():
    if request.method =='POST':
        # player = request.form['play']
        print(request.form)
    else:
        return "hello"

@app.route('/hwlik',methods = ['POST','GET'])
def play():
    if request.method =='POST':
        pass
    pass

if __name__ == "__main__":
    app.run(debug=True)