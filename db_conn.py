from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker

engine = create_engine("postgresql://postgres.rrszvwnprphovamfvzrs:Senhasupabase2!@aws-0-us-west-1.pooler.supabase.com:6543/postgres", 
                        echo=False,
                        pool_size=10,
                        max_overflow=2,
                        pool_recycle=300,
                        pool_pre_ping=True,
                        pool_use_lifo=True,
                        )
session = Session(engine)
scoped_session_factory = sessionmaker(bind=engine)
scoped_session_to_use = scoped_session(scoped_session_factory)

