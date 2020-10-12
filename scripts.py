from app.db import Database
from app.db_models import Wallet


if __name__ == '__main__':
    
    engine, session = Database().connect_to_db()

    session.add(Wallet(name='test', balance=10))
    session.add(Wallet(name='test1', balance=15))
    session.add(Wallet(name='test2', balance=25))

    wallets = session.query(Wallet).all()

    session.close()

    print(wallets)