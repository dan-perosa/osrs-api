from db_conn import scoped_session_to_use
from models import Monster
from sqlalchemy import select
import random

already_in_list_monsters = {}

def take_comma_and_transform(result):
    to_return = result
    if ',' in result:
        to_return = result.replace(',', '')
    
    return int(to_return)

def is_monster_duplicate(monster_info, monster_to_check_name):
    monster_to_check = already_in_list_monsters[monster_to_check_name]
    if (monster_info.members == monster_to_check['members'] and 
        int(take_comma_and_transform(monster_info.combat_level)) == int(monster_to_check['combat_level']) and 
        int(take_comma_and_transform(monster_info.hitpoints)) == int(monster_to_check['hitpoints']) and 
        int(take_comma_and_transform(monster_info.attack_level)) == int(monster_to_check['attack_level']) and 
        int(take_comma_and_transform(monster_info.defence_level)) == int(monster_to_check['defence_level']) and 
        int(take_comma_and_transform(monster_info.magic_level)) == int(monster_to_check['magic_level']) and 
        int(take_comma_and_transform(monster_info.ranged_level)) == int(monster_to_check['ranged_level']) and 
        int(take_comma_and_transform(monster_info.stab_defence)) == int(monster_to_check['stab_defence']) and 
        int(take_comma_and_transform(monster_info.slash_defence)) == int(monster_to_check['slash_defence']) and 
        int(take_comma_and_transform(monster_info.crush_defence)) == int(monster_to_check['crush_defence']) and 
        int(take_comma_and_transform(monster_info.magic_defence)) == int(monster_to_check['magic_defence']) and 
        int(take_comma_and_transform(monster_info.light_ranged_defence)) == int(monster_to_check['light_ranged_defence']) and 
        int(take_comma_and_transform(monster_info.standard_ranged_defence)) == int(monster_to_check['standard_ranged_defence']) and 
        int(take_comma_and_transform(monster_info.heavy_ranged_defence)) == int(monster_to_check['heavy_ranged_defence'])): 
            return True
    return False

def found_daily_monster():
    
    q = select(Monster).order_by(Monster.monster_name)
    results = scoped_session_to_use.execute(q).scalars().all()
    monsters = []
    for result in results:
        monster_name_without_par = result.monster_name.split('(')[0].strip()
        if monster_name_without_par not in list(already_in_list_monsters.keys()):
            already_in_list_monsters[monster_name_without_par] = {
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
        }
        else:
            if is_monster_duplicate(result, monster_name_without_par):
                continue

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
    
    monster_list_length = len(monsters)
    random_monster_number = random.randint(1, monster_list_length)
    
    monster_to_choose = monsters[random_monster_number]
    
    monster = {
            'id': monster_to_choose['id'],
            'image': monster_to_choose['image'],
            'monster_name': monster_to_choose['monster_name'],
            'members': monster_to_choose['members'],
            'combat_level': monster_to_choose['combat_level'],
            'hitpoints': monster_to_choose['hitpoints'],
            'attack_level': monster_to_choose['attack_level'],
            'defence_level': monster_to_choose['defence_level'],
            'magic_level': monster_to_choose['magic_level'],
            'ranged_level': monster_to_choose['ranged_level'],
            'stab_defence': monster_to_choose['stab_defence'],
            'slash_defence': monster_to_choose['stab_defence'],
            'crush_defence': monster_to_choose['crush_defence'],
            'magic_defence': monster_to_choose['magic_defence'],
            'light_ranged_defence': monster_to_choose['light_ranged_defence'],
            'standard_ranged_defence': monster_to_choose['standard_ranged_defence'],
            'heavy_ranged_defence': monster_to_choose['heavy_ranged_defence'],
    }

    scoped_session_to_use.close()
    return monster