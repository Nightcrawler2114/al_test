from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('postgres://superuser:superuser@localhost:5433/al-test-3')

#5433

class Database():

    def connect_to_db(self):

        Session = sessionmaker(bind=engine)

        return engine, Session()
