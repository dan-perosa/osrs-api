from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import text

engine = create_engine("postgresql://postgres.rrszvwnprphovamfvzrs:Senhasupabase2!@aws-0-us-west-1.pooler.supabase.com:6543/postgres", echo=False)
session = Session(engine)

