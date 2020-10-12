from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class Wallet(Base):

    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Float)

    transactions_sent = relationship("TransactionRequest", back_populates="sender", foreign_keys='[TransactionRequest.sender_id]', lazy='subquery')
    transactions_received = relationship("TransactionRequest", back_populates="recipient", foreign_keys='[TransactionRequest.recipient_id]', lazy='subquery')

    def __repr__(self):
        return f'Wallet: "{self.name}/{self.id}"; Available funds: {self.balance}'


class TransactionRequest(Base):

    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('wallets.id'))
    recipient_id = Column(Integer, ForeignKey('wallets.id'))
    amount = Column(Float)

    sender = relationship("Wallet", back_populates="transactions_sent", foreign_keys=[sender_id])
    recipient = relationship("Wallet", back_populates="transactions_received", foreign_keys=[recipient_id])


    def __repr__(self):
        return f'Request ID:{self.id}; Amount: {self.amount}'

