from flask import Flask,request ,jsonify, make_response, redirect, session, url_for
from flask_cors import CORS, cross_origin
from game import Game


app = Flask(__name__)
CORS(app)
app.secret_key = "hello"
gameRound = Game()

@app.route('/play',methods = ['POST','GET',"OPTIONS"])
def index():
    if request.method == "POST": 
        playerChoice = request.json['strat']
        print("playerChose ",playerChoice)
        # print(playerChoice)
        if gameRound.count <3:
            gameRound.machineChoice = gameRound.makeAPlay(playerChoice)
        print("playerChose ",gameRound.machineChoice)
        if gameRound.count == 3:
            if gameRound.scoreMachine < gameRound.scorePlayer :
                gameRound.winner = "player"
            elif gameRound.scoreMachine > gameRound.scorePlayer:
                gameRound.winner = "bot"
            else:
                gameRound.winner = "tie"
        # session['machineChoice'] = machineChoice
        print(gameRound.winner)
        
        return redirect(url_for('index'))
    elif request.method == "GET":
        
        # return {"hello":"yes"}
        if gameRound.machineChoice:
           return {"machineChoice":gameRound.machineChoice}
        else : 
            return {"hello":"yes"}


if __name__ == "__main__":
    app.run(debug=True)