from db_conn import session
from models import User
from flask import jsonify
from sqlalchemy import select, update
from werkzeug.security import check_password_hash
import jwt

jwt_key = 'secret'

def sum_score(user_info):
    score = user_info['score']
    token = user_info['token']
    full_list = user_info['list']
    username = jwt.decode(token, jwt_key, algorithms='HS256')['user']
    
    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    if len(results) == 0:
        return jsonify({'message': 'Username not found'})
    
    previous_score = results[0].score
    new_score = previous_score + score

    q = update(User).where(User.username == username).values(score=new_score)
    session.execute(q)
    session.commit()

    return jsonify({'message': 'points_updated'})


    