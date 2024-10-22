from db_conn import session
from models import User
from flask import jsonify
from sqlalchemy import select, update
import jwt

jwt_key = 'secret'

def logout(user_info):
    token = user_info['token']
    username = jwt.decode(token, jwt_key, algorithms='HS256')['user']
    
    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    if len(results) == 0:
        return jsonify({'message': 'Username not found'})

    q = update(User).where(User.username == username).values(jwt_token='')
    session.execute(q)
    session.commit()

    return jsonify({'message': 'logged out'})


    