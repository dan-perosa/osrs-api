from db_conn import session
from models import Equipment
from sqlalchemy import select
from flask import jsonify

def filter_hashtag_and_count(complete_list):
    filtered_complete_list = []
    has_hashtag_list = []
    for item in complete_list:
        if '#' in item['equipment_name']:
            print('achei o item: ', item['equipment_name'])
            if item['equipment_name'].split('#')[0] in has_hashtag_list:
                print('item ignorado: ', item['equipment_name'])
                continue
            else:
                print('item adicionado e colocado na lista: ', item['equipment_name'])
                has_hashtag_list.append(item['equipment_name'].split('#')[0])
                item['equipment_name'] = item['equipment_name'].split('#')[0]
                filtered_complete_list.append(item)
                continue
        filtered_complete_list.append(item)
    return filtered_complete_list

def get_all_ammunition_equipment():
    q = select(Equipment).where(Equipment.slot == 'Ammunition')
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
    return jsonify(filtered_equipments)