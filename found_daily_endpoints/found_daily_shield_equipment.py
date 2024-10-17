from db_conn import session
from models import Equipment
from sqlalchemy import select
from sqlalchemy.sql.expression import func
import random

def filter_hashtag_and_count(complete_list):
    filtered_complete_list = []
    has_hashtag_list = []
    for item in complete_list:
        if '#' in item['equipment_name']:
            if item['equipment_name'].split('#')[0] in has_hashtag_list:
                continue
            else:
                has_hashtag_list.append(item['equipment_name'].split('#')[0])
                item['equipment_name'] = item['equipment_name'].split('#')[0]
                filtered_complete_list.append(item)
                continue
        filtered_complete_list.append(item)
    return filtered_complete_list

def found_daily_shield_equipment():
    # q = select(Equipment).where(Equipment.slot == 'Shield')
    # shield_equipment_list_length = len(session.execute(q).scalars().all())
    q = select(Equipment).where(Equipment.slot == 'Shield')
    results = session.execute(q).scalars().all()
    equipments = []

    for result in results:
        equipments.append({
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
    
    filtered_equipments = filter_hashtag_and_count(equipments)
    random_equipment_number = random.randint(1, len(filtered_equipments))
    equipment = filtered_equipments[random_equipment_number]
    return equipment