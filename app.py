from flask import Flask, jsonify
from get_all_endpoints.get_all_quests import get_all_quests
from get_specific_endpoints.get_specific_quest import get_specific_quest
from get_all_endpoints.get_all_monsters import get_all_monsters
from get_specific_endpoints.get_specific_monster import get_specific_monster
from get_all_endpoints.get_all_equipments import get_all_equipments
from get_specific_endpoints.get_specific_equipment import get_specific_equipment
from get_all_endpoints.get_all_head_equipment import get_all_head_equipment
from get_all_endpoints.get_all_cape_equipment import get_all_cape_equipment
from get_all_endpoints.get_all_neck_equipment import get_all_neck_equipment
from get_all_endpoints.get_all_ammunition_equipment import get_all_ammunition_equipment
from get_all_endpoints.get_all_weapon_equipment import get_all_weapon_equipment
from get_all_endpoints.get_all_shield_equipment import get_all_shield_equipment
from get_all_endpoints.get_all_two_handed_equipment import get_all_two_handed_equipment
from get_all_endpoints.get_all_body_equipment import get_all_body_equipment
from scheduler_functions.scheduler import scheduler
import scheduler_functions.scheduler as sc
from flask_cors import CORS

app = Flask(__name__)
CORS(app, allow_headers='http://127.0.0.1:3000')

scheduler.start()

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

# equipments

@app.route("/equipments/", methods=['GET'])
def get_all_equipments_endpoint():
    return get_all_equipments()

@app.route("/equipments/<equipment_id>", methods=['GET'])
def get_specific_equipment_endpoint(equipment_id):
    return get_specific_equipment(equipment_id)

@app.route("/equipments/head", methods=['GET'])
def get_all_head_equipment_endpoint():
    return get_all_head_equipment()

@app.route("/equipments/cape", methods=['GET'])
def get_all_cape_equipment_endpoint():
    return get_all_cape_equipment()

@app.route("/equipments/neck", methods=['GET'])
def get_all_neck_equipment_endpoint():
    return get_all_neck_equipment()

@app.route("/equipments/ammunition", methods=['GET'])
def get_all_ammunition_equipment_endpoint():
    return get_all_ammunition_equipment()

@app.route("/equipments/weapon", methods=['GET'])
def get_all_weapon_equipment_endpoint():
    return get_all_weapon_equipment()

@app.route("/equipments/shield", methods=['GET'])
def get_all_shield_equipment_endpoint():
    return get_all_shield_equipment()

@app.route("/equipments/two_handed", methods=['GET'])
def get_all_two_handed_equipment_endpoint():
    return get_all_two_handed_equipment()

@app.route("/equipments/body", methods=['GET'])
def get_all_body_equipment_endpoint():
    return get_all_body_equipment()

# dailies

@app.route("/daily_quest/", methods=['GET'])
def get_daily_quest_endpoint():
    return jsonify(sc.daily_quest)

@app.route("/daily_monster/", methods=['GET'])
def get_daily_monster_endpoint():
    return jsonify(sc.daily_monster)

@app.route("/daily_equipment/", methods=['GET'])
def get_daily_equipment_endpoint():
    return jsonify(sc.daily_equipment)

@app.route("/daily_head_equipment/", methods=['GET'])
def get_daily_head_equipment_endpoint():
    return jsonify(sc.daily_head_equipment)

@app.route("/daily_cape_equipment/", methods=['GET'])
def get_daily_cape_equipment_endpoint():
    return jsonify(sc.daily_cape_equipment)

@app.route("/daily_neck_equipment/", methods=['GET'])
def get_daily_neck_equipment_endpoint():
    return jsonify(sc.daily_neck_equipment)

@app.route("/daily_ammunition_equipment/", methods=['GET'])
def get_daily_ammunition_equipment_endpoint():
    return jsonify(sc.daily_ammunition_equipment)

@app.route("/daily_weapon_equipment/", methods=['GET'])
def get_daily_weapon_equipment_endpoint():
    return jsonify(sc.daily_weapon_equipment)

@app.route("/daily_shield_equipment/", methods=['GET'])
def get_daily_shield_equipment_endpoint():
    return jsonify(sc.daily_shield_equipment)

@app.route("/daily_two_handed_equipment/", methods=['GET'])
def get_daily_two_handed_equipment_endpoint():
    return jsonify(sc.daily_two_handed_equipment)

@app.route("/daily_body_equipment/", methods=['GET'])
def get_daily_body_equipment_endpoint():
    return jsonify(sc.daily_body_equipment)

if __name__ == '__main__':
    app.run()
