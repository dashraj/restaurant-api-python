from flask_restx import fields
from server.instance import server

item = server.api.model("Item",{
    'item_name': fields.String(description='Item Name'),    
    'preparation_time': fields.Integer(description='Preparation time'),
    'quantity': fields.Integer(description='Quantity'),
})

class Item:
    def __init__(self, item_name, time, quantity):
        self.item_name = item_name
        self.preparation_time = time
        self.quantity = quantity

    def to_dict(self):
        return {'item_name': self.item_name, 'preparation_time': self.preparation_time , 'quantity': self.quantity}
