from db_conn import session
from models import User
from flask import jsonify
from sqlalchemy import select, update
import jwt
import datetime
import json
import pprint

jwt_key = 'secret'

def check_existing_victory(user_info):
    token = user_info['token']
    minigame = user_info['minigame']
    username = jwt.decode(token, jwt_key, algorithms='HS256')['user']
    
    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    if len(results) == 0:
        return jsonify({'message': 'Username not found'})
    
    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    list_of_completed_minigames = results[0].finished_info
    dict_list_of_completed_minigames = json.loads(list_of_completed_minigames)
    selected_list = ''
    if dict_list_of_completed_minigames[minigame]['selected'] != None:
        selected_list = dict_list_of_completed_minigames[minigame]['selected']

    return {'selected_list': selected_list}


    