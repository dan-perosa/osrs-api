from db_conn import session
from models import Equipment
from sqlalchemy import select
from sqlalchemy.sql.expression import func
import random

def found_daily_cape_equipment():
    # q = select(Equipment).where(Equipment.slot == 'Cape')
    # cape_equipment_list_length = len(session.execute(q).scalars().all())
    # random_equipment_number = random.randint(1, cape_equipment_list_length)
    q = select(Equipment).where(Equipment.slot == 'Cape').order_by(func.random()).limit(1)
    results = session.execute(q).scalars().all()

    for result in results:
        equipment = ({
            'id': int(result.id),
            'image': result.image,
            'equipment_name': result.equipment_name,
            'members': result.members,
            'stab_attack': int(result.stab_attack),
            'slash_attack': int(result.slash_attack),
            'crush_attack': int(result.crush_attack),
            'magic_attack': int(result.magic_attack),
            'ranged_attack': int(result.ranged_attack),
            'stab_defence': int(result.stab_defence),
            'slash_defence': int(result.slash_defence),
            'crush_defence': int(result.crush_defence),
            'magic_defence': int(result.magic_defence),
            'ranged_defence': int(result.ranged_defence),
            'strength': int(result.strength),
            'ranged_strength': int(result.ranged_strength),
            'magic_damage': result.magic_damage,
            'prayer': int(result.prayer),
            'weight': float(result.weigth),
        })
    return equipment