from flask import Flask
from get_all_quests import get_all_quests
from get_specific_quest import get_specific_quest
from get_all_monsters import get_all_monsters
from get_specific_monster import get_specific_monster

app = Flask('osrs_api')

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