from pydantic import BaseModel, ValidationError, validator
from typing import List


class TransactionRequestBase(BaseModel):
    
    sender_id: int
    recipient_id: int
    amount: int
    
    class Config:
        orm_mode = True


class WalletBase(BaseModel):

    name: str
    balance: int
    transactions_sent: List[TransactionRequestBase] = []
    transactions_received: List[TransactionRequestBase] = []

    class Config:
        orm_mode = True



    