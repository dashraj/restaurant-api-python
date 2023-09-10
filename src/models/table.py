import random
from flask_restx import fields
from server.instance import server
from models.item import item, Item

table = server.api.model("Table",{
    'table_id': fields.Integer(readOnly=True, description='Table ID'),
    'items': fields.Raw #Nested(item, description='Items in the table'),
})

class Table:
    def __init__(self,tid):
        self.table_id = tid
        self.items = {}
    
    def add_items(self, item_names):
        for item in item_names:
            if item not in self.items:
                self.add_item(item)
            else:                
                self.items[item].quantity = self.items[item].quantity + 1                           

    def add_item(self, item_name):
        item = Item(item_name, random.randint(5, 14), 1)
        self.items[item_name] = item

    def check_item(self, item_name):
        return self.items.get(item_name)

    def remove_item(self, item_name):
        return self.items.pop(item_name, None)
    
    def to_dict(self):
        return {
            'table_id': self.table_id,
            'items': [item.to_dict() for item in list(self.items.values())]
        }

