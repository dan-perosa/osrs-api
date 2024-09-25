from db_conn import session
from models import Monster
from sqlalchemy import select
from flask import jsonify

def get_all_monsters():
    q = select(Monster)
    results = session.execute(q).scalars().all()
    monsters = []
    for result in results:
        monsters.append({
            'ID': result.id,
            'Image': result.image,
            'Monster Name': result.monster_name,
            'Members': result.members,
            'Combat Level': result.combat_level,
            'Hitpoints': result.hitpoints,
            'Attack Level': result.attack_level,
            'Defence Level': result.defence_level,
            'Magic Level': result.magic_level,
            'Ranged Level': result.ranged_level,
            'Stab Defence': result.stab_defence,
            'Crush Defence': result.crush_defence,
            'Magic Defence': result.magic_defence,
            'Light Ranged Defence': result.light_ranged_defence,
            'Standard Ranged Defence': result.standard_ranged_defence,
            'Heavy Ranged Defence': result.heavy_ranged_defence,
        })
    return jsonify(monsters)