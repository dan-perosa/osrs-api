from db_conn import scoped_session_to_use
from models import User
from sqlalchemy import update

daily_default = '{"quests":{"finished":"","selected":""},"monsters":{"finished":"","selected":""},"equipments":{"finished":"","selected":""},"ammunition":{"finished":"","selected":""},"body":{"finished":"","selected":""},"cape":{"finished":"","selected":""},"feet":{"finished":"","selected":""},"hands":{"finished":"","selected":""},"head":{"finished":"","selected":""},"legs":{"finished":"","selected":""},"neck":{"finished":"","selected":""},"ring":{"finished":"","selected":""},"shield":{"finished":"","selected":""},"two_handed":{"finished":"","selected":""},"weapon":{"finished":"","selected":""}}'


def daily_value_reseter():

    q = update(User).values(finished_info=daily_default)
    scoped_session_to_use.execute(q)
    scoped_session_to_use.commit()
    scoped_session_to_use.close()

    return {'message': 'values reseted'}


    