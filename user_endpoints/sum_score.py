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
    full_list = user_info['list']
    minigame = user_info['minigame']
    username = jwt.decode(token, jwt_key, algorithms='HS256')['user']
    
    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    if len(results) == 0:
        return jsonify({'message': 'Username not found'})
    
    previous_score = results[0].score
    new_score = previous_score + score
    
    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    list_of_completed_minigames = results[0].finished_info
    print(json.dumps(list_of_completed_minigames))
    dumped = json.dumps(list_of_completed_minigames)
    loaded = json.loads(dumped)
    pprint.pprint(loaded)
    # q = update(User).where(User.username == username).values(score=new_score)
    # session.execute(q)
    # session.commit()

    return jsonify({'message': 'points_updated'})


    