from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime, timedelta
from found_daily_endpoints.found_daily_quest import found_daily_quest
from found_daily_endpoints.found_daily_monster import found_daily_monster
from found_daily_endpoints.found_daily_equipment import found_daily_equipment
from found_daily_endpoints.found_daily_head_equipment import found_daily_head_equipment
from found_daily_endpoints.found_daily_cape_equipment import found_daily_cape_equipment
from found_daily_endpoints.found_daily_neck_equipment import found_daily_neck_equipment
from found_daily_endpoints.found_daily_ammunition_equipment import found_daily_ammunition_equipment
from found_daily_endpoints.found_daily_weapon_equipment import found_daily_weapon_equipment
from found_daily_endpoints.found_daily_shield_equipment import found_daily_shield_equipment
from found_daily_endpoints.found_daily_two_handed_equipment import found_daily_two_handed_equipment
from found_daily_endpoints.found_daily_body_equipment import found_daily_body_equipment
from found_daily_endpoints.found_daily_legs_equipment import found_daily_legs_equipment
from found_daily_endpoints.found_daily_hands_equipment import found_daily_hands_equipment
from found_daily_endpoints.found_daily_feet_equipment import found_daily_feet_equipment


scheduler = BackgroundScheduler()

def get_daily_quest():
    global daily_quest
    daily_quest = found_daily_quest()
scheduler.add_job(
    func=get_daily_quest,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_monster():
    global daily_monster
    daily_monster = found_daily_monster()
scheduler.add_job(
    func=get_daily_monster,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_equipment():
    global daily_equipment
    daily_equipment = found_daily_equipment()
scheduler.add_job(
    func=get_daily_equipment,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_head_equipment():
    global daily_head_equipment
    daily_head_equipment = found_daily_head_equipment()
scheduler.add_job(
    func=get_daily_head_equipment,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_cape_equipment():
    global daily_cape_equipment
    daily_cape_equipment = found_daily_cape_equipment()
scheduler.add_job(
    func=get_daily_cape_equipment,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_neck_equipment():
    global daily_neck_equipment
    daily_neck_equipment = found_daily_neck_equipment()
scheduler.add_job(
    func=get_daily_neck_equipment,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_ammunition_equipment():
    global daily_ammunition_equipment
    daily_ammunition_equipment = found_daily_ammunition_equipment()
scheduler.add_job(
    func=get_daily_ammunition_equipment,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_weapon_equipment():
    global daily_weapon_equipment
    daily_weapon_equipment = found_daily_weapon_equipment()
scheduler.add_job(
    func=get_daily_weapon_equipment,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_shield_equipment():
    global daily_shield_equipment
    daily_shield_equipment = found_daily_shield_equipment()
scheduler.add_job(
    func=get_daily_shield_equipment,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_two_handed_equipment():
    global daily_two_handed_equipment
    daily_two_handed_equipment = found_daily_two_handed_equipment()
scheduler.add_job(
    func=get_daily_two_handed_equipment,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_body_equipment():
    global daily_body_equipment
    daily_body_equipment = found_daily_body_equipment()
scheduler.add_job(
    func=get_daily_body_equipment,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_legs_equipment():
    global daily_legs_equipment
    daily_legs_equipment = found_daily_legs_equipment()
scheduler.add_job(
    func=get_daily_legs_equipment,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_hands_equipment():
    global daily_hands_equipment
    daily_hands_equipment = found_daily_hands_equipment()
scheduler.add_job(
    func=get_daily_hands_equipment,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)

def get_daily_feet_equipment():
    global daily_feet_equipment
    daily_feet_equipment = found_daily_feet_equipment()
scheduler.add_job(
    func=get_daily_feet_equipment,
    trigger=IntervalTrigger(start_date=(datetime.now() - timedelta(minutes=4, seconds=55)) , minutes=5),
)
