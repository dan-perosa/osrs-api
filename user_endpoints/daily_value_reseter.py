from db_conn import scoped_session_to_use
from models import User
from sqlalchemy import update

daily_default = '{"quests":{"finished":"","selected":"", "victory": "False"},"monsters":{"finished":"","selected":"", "victory": "False"},"equipments":{"finished":"","selected":"", "victory": "False"},"ammunition":{"finished":"","selected":"", "victory": "False"},"body":{"finished":"","selected":"", "victory": "False"},"cape":{"finished":"","selected":"", "victory": "False"},"feet":{"finished":"","selected":"", "victory": "False"},"hands":{"finished":"","selected":"", "victory": "False"},"head":{"finished":"","selected":"", "victory": "False"},"legs":{"finished":"","selected":"", "victory": "False"},"neck":{"finished":"","selected":"", "victory": "False"},"ring":{"finished":"","selected":"", "victory": "False"},"shield":{"finished":"","selected":"", "victory": "False"},"two_handed":{"finished":"","selected":"", "victory": "False"},"weapon":{"finished":"","selected":"", "victory": "False"}}'


def daily_value_reseter():

    q = update(User).values(finished_info=daily_default)
    scoped_session_to_use.execute(q)
    scoped_session_to_use.commit()
    scoped_session_to_use.close()

    return {'message': 'values reseted'}


    