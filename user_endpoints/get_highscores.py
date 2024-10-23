from db_conn import session
from models import User
from flask import jsonify
from sqlalchemy import select


def get_highscores():   
    q = select(User).order_by(User.score)
    results = session.execute(q).scalars().all()
    highscores = []
    
    for result in results:
        highscores.append({
            'user': result.username,
            'score': 0 if result.score==None else result.score,
        })
     
    return jsonify(highscores)
    