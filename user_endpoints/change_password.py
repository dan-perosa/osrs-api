from db_conn import session
from models import User
from flask import jsonify
from sqlalchemy import select, update
from werkzeug.security import check_password_hash, generate_password_hash


def change_password(user_info):
    username = user_info['username']
    old_password = user_info['old_password']
    new_password = user_info['new_password']

    q = select(User).where(User.username == username)
    results = session.execute(q).scalars().all()
    hashed_password = results[0].password
    correct_password = check_password_hash(pwhash=hashed_password, password=old_password)
    if not correct_password:
        return jsonify({'message': 'wrong password'})
    
    q = update(User).where(User.username == username).values(password=generate_password_hash(new_password))
    session.execute(q)
    session.commit()
    
    return jsonify({'message': 'password changed'})


    