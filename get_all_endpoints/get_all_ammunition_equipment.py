from db_conn import session
from models import Equipment
from sqlalchemy import select
from flask import jsonify

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
    return jsonify(equipments)