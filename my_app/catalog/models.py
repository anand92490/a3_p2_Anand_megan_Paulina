
from my_app import db
from sqlalchemy.orm import relationship
from datetime import datetime


association_table = db.Table(
    "association_table",
    db.Column("customrTicket_id", db.ForeignKey("customer_ticket.id"), primary_key=True),
    db.Column("menu_id", db.ForeignKey("menu.id"), primary_key=True),
)

class Waiter(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    tax_number = db.Column(db.Float)
    customer_ticket_id = db.Column(db.Integer, db.ForeignKey('customer_ticket.id'))
    customer_ticket = db.relationship('CustomerTicket', backref=db.backref('waiter',lazy='dynamic')) #, uselist=False will assign only one waiter(parent) for each customer(child)

    def __init__(self, first_name, last_name, tax_number):
        self.first_name = first_name
        self.last_name = last_name
        self.tax_number = tax_number 
        
    def __repr__(self):
        return '<Waiter %d>' % self.id


class CustomerTicket(db.Model):
    __tablename__ = "customer_ticket"

    id = db.Column(db.Integer, primary_key=True)
    arrival = db.Column(db.DateTime)
    departed = db.Column(db.DateTime)
    table_no = db.Column(db.Integer)
    menu = relationship('Menu',
       secondary=association_table, back_populates='customer_ticket'
    )

    def __init__(self, arrival, departed, table_no):
        self.arrival = arrival
        self.departed = departed
        self.table_no = table_no
    def __repr__(self):
        return '<CustomerTicket %d>' % self.id


class Menu(db.Model):
    __tablename__ = "menu"
    
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Numeric)
    customer_ticket = relationship('CustomerTicket',
       secondary=association_table,  back_populates='menu'
    )

    def __init__(self, item_name, description, price):
        self.item_name = item_name
        self.description = description
        self.price = price  

    def __repr__(self):
        return '<CustomerTicket %d>' % self.id
