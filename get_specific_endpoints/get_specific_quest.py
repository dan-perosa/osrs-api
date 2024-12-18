from db_conn import session
from models import Quest
from sqlalchemy import select
from flask import jsonify

def get_specific_quest(quest_id):
    q = select(Quest).where(Quest.id == quest_id)
    results = session.execute(q).scalars().all()

    for result in results:
        quest = ({
            'ID': result.id,
            'Name': result.name,
            'Difficulty': result.difficulty,
            'Length': result.length,
            'Quest Points': result.quest_points,
            'Series': result.series,
            'Release Date': result.release_date,
        })
    return jsonify(quest)