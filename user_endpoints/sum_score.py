from db_conn import session
from models import User
from flask import jsonify
from sqlalchemy import select, update
import jwt
import datetime
import json
import pprint

jwt_key = 'secret'

def sum_score(user_info):
    score = user_info['score']
    token = user_info['token']
    present_minigame_selected_list = user_info['list']
    minigame = user_info['minigame']
    username = jwt.decode(token, jwt_key, algorithms='HS256')['user']
    victory = user_info['victory']
    
    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    if len(results) == 0:
        return jsonify({'message': 'Username not found'})
    
    previous_score = results[0].score
    new_score = previous_score + score
    
    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    list_of_completed_minigames: str = results[0].finished_info
    dict_list_of_completed_minigames = json.loads(list_of_completed_minigames.replace("'", '').replace('None', 'null'))
    dict_list_of_completed_minigames[minigame] = {
        'finished': datetime.datetime.now(),
        'selected': present_minigame_selected_list,
        'victory': victory
    }
    dumped_dict_to_return = json.dumps(dict_list_of_completed_minigames, default=str)
    
    
    q = update(User).where(User.username == username).values(score=new_score, finished_info=dumped_dict_to_return)
    session.execute(q)
    session.commit()

    return jsonify({'message': 'points_updated'})


    