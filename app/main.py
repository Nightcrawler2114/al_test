from fastapi import FastAPI, Depends

from typing import List

from app.models import WalletBase, TransactionRequestBase

from app.db import Database, Base, engine
from app.db_models import Wallet as WalletModel, TransactionRequest as TransactionRequestModel

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/", response_model=List[WalletBase])
async def wallets_list() -> List[WalletBase] == []:
    
    engine, session = Database().connect_to_db()
    wallets = session.query(WalletModel).all()

    session.close()

    return wallets


@app.post("/make-transaction/")
async def make_transaction(sender: int, recipient: int, amount: float) -> dict:

    commission = 0.015

    engine, session = Database().connect_to_db()

    sender_ = session.query(WalletModel).filter_by(id=sender).first() 
    recipient_ = session.query(WalletModel).filter_by(id=recipient).first() 

    if not sender_:

        return {'error': 'Sender wallet does not exists'}

    if not recipient_:

        return {'error': 'Recipient wallet does not exists'}

    if sender == recipient:

        return {'error': 'Choose different recepient or sender'}

    if amount > sender_.balance:

        return {'error': 'Insufficient funds'}

    transaction_request =  TransactionRequestModel(sender=sender_, recipient=recipient_, amount=amount)
    session.add(transaction_request)

    amount_after_commission = amount * (1 - commission)

    sender_.balance -= amount_after_commission
    recipient_.balance += amount

    session.commit()
    session.refresh(sender_)
    session.refresh(recipient_)
    session.close()

    return {"success": f"{amount} has been successfuly transfered to wallet {recipient_.id}"}