from flask import Flask
from flask import request

top_games = {
                1:{
                    "title":"Red Dead Redemption II",
                    "rating":9.7,
                    "released":2018,
                    "description":"Amidst the decline of the Wild West at the turn of the 20th century, outlaw Arthur Morgan and his gang struggle to cope with the loss of their way of life."
                },
                2:{
                    "title":"The Last of Us",
                    "rating":9.7,
                    "released":2013,
                    "description":"In a hostile, post-pandemic world, Joel and Ellie, brought together by desperate circumstances, must rely on each other to survive a brutal journey across what remains of the United States."
                },
                3:{
                    "title":"The Witcher 3: Wild Hunt",
                    "rating":9.7,
                    "released":2015,
                    "description":"A monster slayer must find his adoptive daughter, a living weapon that can bring the world to an end."
                },
                4:{
                    "title":"Baldur's Gate III",
                    "rating":9.7,
                    "released":2023,
                    "description":"Return to the Faerun in a tale of fellowship and betrayal, and the lure of absolute power. Mysterious abilities are awakening inside you. Resist, and turn darkness against itself. Or embrace corruption, and become ultimate evil."
                },
                5:{
                    "title":"Metal Gear Solid",
                    "rating":9.6,
                    "released":1998,
                    "description":"A crack government anti-terrorist squad takes over an obscure Alaskan nuclear disposal facility. Solid Snake is up for the task to infiltrate the facility, rescue the two hostages and thwart the terrorists' plans."
                }
            }

app = Flask(__name__)

@app.route("/top_games/<rank>", methods = ["GET","PUT","DELETE"])
def top_games_with_arg(rank):
        if request.method == "GET":
            return top_games[int(rank)]
        elif request.method == "PUT":
            top_games[int(rank)] = request.get_json()
            return "Success"
        elif request.method == "DELETE":
            top_games.pop(int(rank))
            return "Success"
        return "?"

@app.route("/top_games", methods = ["GET","POST"])
def top_games_no_arg():
        if request.method == "GET":
            return top_games
        elif request.method == "POST":
            top_games[len(top_games)+1] = request.get_json()
            #top_games[6] = request.get_json()
            return "Success"


if __name__ == "__main__":
    app.run(port=80)
