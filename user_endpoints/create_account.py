from db_conn import session
from models import User
from flask import jsonify
from sqlalchemy import select
from werkzeug.security import generate_password_hash


def create_account(user_info):
    username = user_info['username']
    password = user_info['password']
    hashed_password = generate_password_hash(password)
    
    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    
    if len(results) > 0:
        return jsonify({'message': 'Username already registered'})
    if len(username) > 20:
        return jsonify({'message': 'Username needs to be shorter than 20 characters'})
    if len(password) > 30:
        return jsonify({'message': 'Password needs to be shorter than 30 characters'})

    user = User(username=username, password=hashed_password)
    
    try:
        session.add(user)
        session.commit()
        return jsonify({'message': 'created'})
    except:
        return jsonify({'message': 'unable to create'})
    