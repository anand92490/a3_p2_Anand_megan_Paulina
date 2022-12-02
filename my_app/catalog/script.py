from sqlalchemy.orm import sessionmaker
from my_app import db
from models import *

Session = sessionmaker(bind = db)
session = Session()

waiter = Waiter("Lionel", "Messi", 1234587384)
session.add(waiter)

# tshirt, mug, hat, crowbar = (
#     Item("SA T-Shirt", 10.99),
#     Item("SA Mug", 6.50),
#     Item("SA Hat", 8.99),
#     Item("SA Crowbar", 16.99),
# )
# session.add_all([tshirt, mug, hat, crowbar])
session.commit()

# # create an order
# order = Order("John Smith")

# # add three OrderItem associations to the Order and save
# order.items.append(tshirt)
# order.items.append(mug)
# order.items.append(hat)

# order2 = Order("Sunyung Lee")
# order2.items.append(tshirt)
# order2.items.append(mug)

# session.add(order)
# session.add(order2)
# session.commit()

