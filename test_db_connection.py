from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db_models import Wallet


engine = create_engine('postgres://superuser:superuser@localhost:5433/al-test-3')

Session = sessionmaker(bind=engine)

session = Session()

wallets = session.query(Wallet).all()

print(wallets)
