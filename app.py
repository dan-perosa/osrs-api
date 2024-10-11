from flask import Flask, jsonify
from get_all_quests import get_all_quests
from get_specific_quest import get_specific_quest
from get_all_monsters import get_all_monsters
from get_specific_monster import get_specific_monster
from get_all_equipments import get_all_equipments
from get_specific_equipment import get_specific_equipment
from found_daily_quest import found_daily_quest
from found_daily_monster import found_daily_monster
from found_daily_equipment import found_daily_equipment
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime, timedelta
import random
import time

app = Flask(__name__)
CORS(app, allow_headers='http://127.0.0.1:3000')

scheduler = BackgroundScheduler()

def get_daily_quest():
    global daily_quest
    daily_quest = found_daily_quest()
    print(daily_quest)
    
scheduler.add_job(
    func=get_daily_quest,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_monster():
    global daily_monster
    daily_monster = found_daily_monster()
    print(daily_monster)
    
scheduler.add_job(
    func=get_daily_monster,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_equipment():
    global daily_equipment
    daily_equipment = found_daily_equipment()
    print(daily_equipment)
    
scheduler.add_job(
    func=get_daily_equipment,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

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

@app.route("/equipments/", methods=['GET'])
def get_all_equipments_endpoint():
    return get_all_equipments()

@app.route("/equipments/<equipment_id>", methods=['GET'])
def get_specific_equipment_endpoint(equipment_id):
    return get_specific_equipment(equipment_id)

@app.route("/daily_quest/", methods=['GET'])
def get_daily_quest_endpoint():
    return jsonify(daily_quest)

@app.route("/daily_monster/", methods=['GET'])
def get_daily_monster_endpoint():
    return jsonify(daily_monster)

@app.route("/daily_equipment/", methods=['GET'])
def get_daily_equipment_endpoint():
    return jsonify(daily_equipment)

if __name__ == '__main__':
    app.run()
