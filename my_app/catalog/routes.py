from flask import request, jsonify, Blueprint #blueprint helps to modularize different routes for you
from my_app import db
from datetime import datetime
from my_app.catalog.models import Waiter, CustomerTicket, Menu, association_table
import json



catalog = Blueprint('catalog', __name__)

@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the POS system."

#view waiter by id 
@catalog.route('/Waiter/<id>')
def waiter(id):
    waiter = Waiter.query.get_or_404(id)
    return 'Waiter - %s, $%s' % (waiter.first_name, waiter.last_name,waiter.tax_number)


#view menu item by id
@catalog.route('/menu-item/<id>')
def menu_item(id):
    menu_item = Menu.query.get_or_404(id)
    return 'Menu - %s, $%s' % (menu_item.item_name, menu_item.description, menu_item.price)


#view ticket by id
@catalog.route('/customer-ticket/<id>')
def ticket(id):
    ticket = CustomerTicket.query.get_or_404(id)
    return 'CustomerTicket - %s, $%s' % (ticket.arrival, ticket.departed, ticket.table_no)


#show all waiters
@catalog.route('/show-waiters')
def waiters():
    waiters = Waiter.query.all()
    res = {}
    for waiter in waiters:
        res[waiter.id] = {
            'first_name': waiter.first_name,
            'last_name': waiter.last_name,
            'tax_number': waiter.tax_number
        }
    return jsonify(res)


#show all menu items 
@catalog.route('/show-menu')
def menu_items():
    menu_items = Menu.query.all()
    res = {}
    for menu_item in menu_items:
        res[menu_item.id] = {
            'item_name': menu_item.item_name,
            'description': menu_item.description,
            'price': menu_item.price
        }
    return jsonify(res)

#show all customer tickets 
@catalog.route('/show-tickets')
def tickets():
    tickets = CustomerTicket.query.all()
    res = {}
    for ticket in tickets:
        res[ticket.id] = {
            'arrival': ticket.arrival,
            'departed': ticket.departed,
            'table_no': ticket.table_no
        }
    return jsonify(res)

#create waiter 
@catalog.route('/create-waiter', methods=['POST',])
def create_waiter():
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    tax_number = request.json.get('tax_number')

    waiter = Waiter(first_name, last_name, tax_number)
    db.session.add(waiter)
    db.session.commit()
    return 'Waiter created'



#add single item to the menu 
@catalog.route('/single-menu', methods=['POST',])
def single_menu():
    item_name = request.json.get('item_name')
    description = request.json.get('description')
    price = request.json.get('price')

    menu = Menu(item_name,description, price)
    db.session.add(menu)
    db.session.commit()
    return 'Menu created.'


#create multiple menu items
@catalog.route('/create-menus', methods=['POST',])
def create_menu():
    import json
    data = json.loads(request.data)

    for menu_items in data:
        key = data[menu_items]

        item_name = key['item_name']
        description = key['description']
        price = key['price']
       
        menu = Menu(item_name, description, price)

        db.session.add(menu)
        db.session.commit()
            
    return "Multiple Menu items created."


#create customer ticket 
@catalog.route('/create-customer-ticket', methods=['POST',])
def create_ticket():
    import json
    arrival = request.json.get('arrival')
    departed = request.json.get('departed')
    new_arrival = datetime.strptime(arrival, "%Y-%m-%d %H:%M:%S")
    new_departed = datetime.strptime(departed, "%Y-%m-%d %H:%M:%S")
    table_no = request.json.get('table_no')
    name = request.json.get('name')
    ticket = CustomerTicket(new_arrival, new_departed, table_no)
    choice = Menu.query.filter_by(item_name=name).first()
    if choice:
        ticket.menu.append(choice)
        db.session.add(ticket)
        db.session.commit()
    
    # data = json.loads(request.data)
    # arrival = data['arrival']
    # departed = data['departed']
    # new_arrival = datetime.strptime(arrival, "%Y-%m-%d %H:%M:%S")
    # new_departed = datetime.strptime(departed, "%Y-%m-%d %H:%M:%S")
    # table_no = data['table_no']
    # opt1 = data['order'][0]
    
    # db.session.add(ticket)
    # db.session.commit()
        
    
    return 'Customer ticket created'
        
    
 
    
    # choice = Menu.query.filter_by(item_name=name).first()
    # if choice:
    #     ticket.menu.append(choice)
    #     db.session.add(ticket)
    #     db.session.commit()
    # choice_two = Menu.query.filter_by(item_name=name_two).first()
    # if choice_two:
    #     ticket.menu.append(choice_two)
    #     db.session.add(ticket)
    #     db.session.commit()
    # for items in food:
    #     key = food[items]
    #     name = key['name']
    #     choice = Menu.query.filter_by(item_name=name).first()
    #     if choice:
    #         ticket.menu.append(choice)
    #         db.session.add(ticket)
    #         db.session.commit()
   
    
    

#make order
# @catalog.route('/create-order', methods=['POST',])
# def order(ticket):
#     orders = json.loads(request.data)

#     for items in orders:

#         key = orders[items]
#         name = key['name']
#         choice = Menu.query.filter_by(item_name=name), first()
#         if choice:
#             ticket.menu.append(choice)
#             db.session.add(ticket)
#             db.session.commit()
#     return "Order completed"


        
            
        




        



