from db_conn import session
from models import Monster
from sqlalchemy import select
from flask import jsonify

def take_comma_and_transform(result):
    to_return = result
    if ',' in result:
        to_return = result.replace(',', '')
    
    return int(to_return)
        

def get_all_monsters():
    q = select(Monster)
    results = session.execute(q).scalars().all()
    monsters = []
    for result in results:
        monsters.append({
            'id': result.id,
            'image': result.image,
            'monster_name': result.monster_name,
            'members': result.members,
            'combat_level': take_comma_and_transform(result.combat_level),
            'hitpoints': take_comma_and_transform(result.hitpoints),
            'attack_level': take_comma_and_transform(result.attack_level),
            'defence_level': take_comma_and_transform(result.defence_level),
            'magic_level': take_comma_and_transform(result.magic_level),
            'ranged_level': take_comma_and_transform(result.ranged_level),
            'stab_defence': take_comma_and_transform(result.stab_defence),
            'slash_defence': take_comma_and_transform(result.slash_defence),
            'crush_defence': take_comma_and_transform(result.crush_defence),
            'magic_defence': take_comma_and_transform(result.magic_defence),
            'light_ranged_defence': take_comma_and_transform(result.light_ranged_defence),
            'standard_ranged_defence': take_comma_and_transform(result.standard_ranged_defence),
            'heavy_ranged_defence': take_comma_and_transform(result.heavy_ranged_defence),
        })
    return jsonify(monsters)