from db_conn import session
from models import Quest
from sqlalchemy import select
import random

def found_daily_quest():
    q = select(Quest)
    quest_list_length = len(session.execute(q).scalars().all())
    random_quest_number = random.randint(1, quest_list_length)
    q = select(Quest).where(Quest.id == random_quest_number)
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
    return quest