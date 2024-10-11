from db_conn import session
from models import Monster
from sqlalchemy import select
import random

def found_daily_monster():
    q = select(Monster)
    monster_list_length = len(session.execute(q).scalars().all())
    random_monster_number = random.randint(1, monster_list_length)
    q = select(Monster).where(Monster.id == random_monster_number)
    results = session.execute(q).scalars().all()

    for result in results:
        monster = ({
            'id': result.id,
            'image': result.image,
            'monster_name': result.monster_name,
            'members': result.members,
            'combat_level': result.combat_level,
            'hitpoints': result.hitpoints,
            'attack_level': result.attack_level,
            'defence_level': result.defence_level,
            'magic_level': result.magic_level,
            'ranged_level': result.ranged_level,
            'stab_defence': result.stab_defence,
            'crush_defence': result.crush_defence,
            'magic_defence': result.magic_defence,
            'light_ranged_defence': result.light_ranged_defence,
            'standard_ranged_defence': result.standard_ranged_defence,
            'heavy_ranged_defence': result.heavy_ranged_defence,
        })
    return monster