from db_conn import session
from models import Equipment
from sqlalchemy import select
import random

def found_daily_equipment():
    q = select(Equipment)
    equipment_list_length = len(session.execute(q).scalars().all())
    random_equipment_number = random.randint(1, equipment_list_length)
    q = select(Equipment).where(Equipment.id == random_equipment_number)
    results = session.execute(q).scalars().all()

    for result in results:
        equipment = ({
            'id': result.id,
            'image': result.image,
            'equipment_name': result.equipment_name,
            'members': result.members,
            'stab_attack': result.stab_attack,
            'slash_attack': result.slash_attack,
            'crush_attack': result.crush_attack,
            'magic_attack': result.magic_attack,
            'ranged_attack': result.ranged_attack,
            'stab_defence': result.stab_defence,
            'slash_defence': result.slash_defence,
            'crush_defence': result.crush_defence,
            'magic_defence': result.magic_defence,
            'ranged_defence': result.ranged_defence,
            'strength': result.strength,
            'ranged_strength': result.ranged_strength,
            'magic_damage': result.magic_damage,
            'prayer': result.prayer,
            'weight': result.weigth,
            'speed': result.speed,
        })
    return equipment