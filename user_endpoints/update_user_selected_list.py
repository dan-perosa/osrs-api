from db_conn import session
from models import User
from flask import jsonify
from sqlalchemy import select, update
import jwt
import datetime
import json
import pprint

jwt_key = 'secret'

def update_user_selected_list(user_info):
    token = user_info['token']
    selected_list = user_info['selected_list']
    minigame = user_info['minigame']
    username = jwt.decode(token, jwt_key, algorithms='HS256')['user']
    
    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    if len(results) == 0:
        return jsonify({'message': 'Username not found'})
    
    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    list_of_completed_minigames: str = results[0].finished_info
    dict_list_of_completed_minigames = json.loads(list_of_completed_minigames.replace("'", '').replace('None', 'null'))
    dict_list_of_completed_minigames[minigame] = {
        'finished': datetime.datetime.now(),
        'selected': selected_list
    }
    dumped_dict_to_return = json.dumps(dict_list_of_completed_minigames, default=str)
    
    
    q = update(User).where(User.username == username).values(finished_info=dumped_dict_to_return)
    session.execute(q)
    session.commit()

    return jsonify({'message': 'selected list updated'})


    