from flask_restx import Resource, fields
from server.instance import server
from models.table import table
from models.order import Order

app, api = server.app, server.api

restaurantOrders = Order()

@api.route('/restaurant')
class RestaurantController(Resource):
    @api.doc('Get all orders')
    def get(self):
        """
        Get all orders
        """
        return  [table.to_dict() for table in restaurantOrders.get_all_tables()], 200

@api.route('/restaurant/<int:table_number>')
class TableController(Resource):
    @api.doc('Get table orders')
    def get(self, table_number):
        """
        Get table's orders
        """
        if table_number in restaurantOrders.tables:
            table = restaurantOrders.get_table(table_number)
            return table.to_dict()

        return {'message': 'Table not found.'}, 404

    @api.doc('Add new Order') 
    @api.expect(api.model('Items', {'items': fields.List(fields.String(required=True))}))   
    def post(self, table_number):
        """
        Add an item to the table
        """
        args = api.payload
        items = args['items']
        restaurantOrders.add_table(table_number,items)
        return {'message': 'Order placed successfully.'}, 201
    
    @api.doc('Remove Items from table\'s Order') 
    @api.expect(api.model('Items', {'items': fields.List(fields.String(required=True))}))   
    def put(self, table_number):
        """
        Remove Items from table's Order
        """
        args = api.payload
        items = args['items']
        if table_number in restaurantOrders.tables: 
            table = restaurantOrders.get_table(table_number)
            table.remove_items(items)
            return {'message': 'Items removed successfully.'}, 201
        return {'message': 'Table not found.'}, 404
    
    @api.doc('Remove an order') 
    def delete(self, table_number):
        """
        Add an item to the table
        """
        if table_number in restaurantOrders.tables:            
            restaurantOrders.remove_table(table_number)
            return {'message': f'Orders for the table {table_number} are removed.'}, 200


@api.route('/restaurant/<int:table_number>/<string:item_name>')
class ItemController(Resource):
    @api.doc('Get item details') 
    def get(self, table_number,item_name):
        """
        Get item details
        """
        if table_number in restaurantOrders.tables:
            table = restaurantOrders.get_table(table_number)
            if item_name in table.items:
                item = table.items[item_name]
                return  item.to_dict()
        return {'message': f'Item {item_name} not found in the table {table_number}.'}, 404 
    
    @api.doc('Add item to the table\'s order') 
    def post(self, table_number,item_name):
        """
        Add item to the table's order.
        """
        print(f'{table_number} - {item_name}')
        restaurantOrders.add_table(table_number,[item_name])
        return {'message' : f'Item {item_name} added to the table {table_number}\'s order.'}
    
    @api.doc('Remove item from the table\'s order') 
    def delete(self, table_number,item_name):
        """
        Remove item from the table's order.
        """
        if table_number in restaurantOrders.tables:
            table = restaurantOrders.get_table(table_number)
            table.remove_items([item_name])
            return {'message' : f'Item {item_name} removed from the table {table_number}\'s order.'}
        return {'message': f'The table {table_number} not found.'}, 404 
