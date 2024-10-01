from flask import Flask
from get_all_quests import get_all_quests
from get_specific_quest import get_specific_quest
from get_all_monsters import get_all_monsters
from get_specific_monster import get_specific_monster
from flask_cors import CORS

app = Flask(__name__)
CORS(app, allow_headers='http://127.0.0.1:3000')

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Origin"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

@app.route("/")
def home():
    return "Flask Vercel Example - Hello World", 200

@app.route("/quests/", methods=['GET'])
def get_all_quests_endpoint():
    return get_all_quests()

@app.route("/quests/<quest_id>", methods=['GET'])
def get_specific_quest_endpoint(quest_id):
    return get_specific_quest(quest_id)

@app.route("/monsters/", methods=['GET'])
def get_all_monsters_endpoint():
    return get_all_monsters()

@app.route("/monsters/<monster_id>", methods=['GET'])
def get_specific_monster_endpoint(monster_id):
    return get_specific_monster(monster_id)

if __name__ == '__main__':
    app.run()