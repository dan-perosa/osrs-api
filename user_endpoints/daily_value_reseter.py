from db_conn import scoped_session_to_use
from models import User
from sqlalchemy import update

daily_default = '{"quests":{"finished":"","selected":"", "victory": false},"monsters":{"finished":"","selected":"", "victory": false},"equipments":{"finished":"","selected":"", "victory": false},"ammunition":{"finished":"","selected":"", "victory": false},"body":{"finished":"","selected":"", "victory": false},"cape":{"finished":"","selected":"", "victory": false},"feet":{"finished":"","selected":"", "victory": false},"hands":{"finished":"","selected":"", "victory": false},"head":{"finished":"","selected":"", "victory": false},"legs":{"finished":"","selected":"", "victory": false},"neck":{"finished":"","selected":"", "victory": false},"ring":{"finished":"","selected":"", "victory": false},"shield":{"finished":"","selected":"", "victory": false},"two_handed":{"finished":"","selected":"", "victory": false},"weapon":{"finished":"","selected":"", "victory": false}}'


def daily_value_reseter():

    q = update(User).values(finished_info=daily_default)
    scoped_session_to_use.execute(q)
    scoped_session_to_use.commit()
    scoped_session_to_use.close()

    return {'message': 'values reseted'}


    