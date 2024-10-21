from db_conn import session
from models import User
from flask import jsonify
from sqlalchemy import select
from werkzeug.security import check_password_hash, generate_password_hash


def login(user_info):
    username = user_info['username']
    password = user_info['password']
    
    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    if len(results) == 0:
        return jsonify({'message': 'username not found'})
    hashed_password = results[0].password
    
    correct_password = check_password_hash(pwhash=hashed_password, password=password)
    if not correct_password:
        return jsonify({'message': 'wrong password'})
    return jsonify({'message': 'logged in'})


    