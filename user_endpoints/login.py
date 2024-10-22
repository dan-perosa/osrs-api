from db_conn import session
from models import User
from flask import jsonify
from sqlalchemy import select, update
from werkzeug.security import check_password_hash
import jwt

jwt_key = 'secret'

def login(user_info):
    username = user_info['username']
    password = user_info['password']
    
    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    if len(results) == 0:
        return jsonify({'message': 'Username not found'})
    hashed_password = results[0].password
    
    correct_password = check_password_hash(pwhash=hashed_password, password=password)
    if not correct_password:
        return jsonify({'message': 'Wrong password'})
    
    encoded_jwt = jwt.encode({
        'user': username
    }, jwt_key, algorithm='HS256')
    
    q = update(User).where(User.username == username).values(jwt_token=encoded_jwt)
    session.execute(q)
    session.commit()

    return jsonify({'message': 'logged',
                    'token': encoded_jwt})


    