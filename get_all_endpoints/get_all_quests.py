from db_conn import session
from models import Quest
from sqlalchemy import select
from flask import jsonify

def get_all_quests():
    q = select(Quest)
    results = session.execute(q).scalars().all()
    quests = []
    for result in results:
        quests.append({
            'ID': result.id,
            'Name': result.name,
            'Difficulty': result.difficulty,
            'Length': result.length,
            'Quest Points': result.quest_points,
            'Series': result.series,
            'Release Date': result.release_date,
        })
    return jsonify(quests)