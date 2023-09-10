from tokenize import String
from flask import Flask, request, jsonify
import random
import threading
from flask_restx import Resource, fields
from server.instance import server
from models.item import item
from models.table import table
from models.order import Order

app, api = server.app, server.api

restaurant = Order()

orders = api.model('Orders', {
    'orders': fields.List(fields.Nested(table))
})

@api.route('/restaurant')
class RestaurantController(Resource):
    @api.doc('Get all orders')
    # @api.marshal_with(orders)
    def get(self):
        """
        Get all orders
        """
        return  [table.to_dict() for table in restaurant.get_all_tables()], 200

@api.route('/restaurant/<int:table_number>')
class TableController(Resource):
    @api.doc('Get table orders')
    # @api.marshal_with(table)
    def get(self, table_number):
        if table_number in restaurant.tables:
            table = restaurant.get_table(table_number)
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
        restaurant.add_table(table_number,items)
        return items
        # return {'message': 'Order placed successfully.'}, 201
    
    @api.doc('Remove an order') 
    def delete(self, table_number):
        """
        Add an item to the table
        """
        if table_number in restaurant.tables:            
            restaurant.remove_table(table_number)
            return {'message': f'Orders for the table {table_number} are removed.'}, 200


@api.route('/restaurant/<int:table_number>/<string:item_name>')
class ItemController(Resource):
    @api.doc('Get item details') 
    def get(self, table_number,item_name):
        """
        Get item details
        """
        if table_number in restaurant.tables:
            table = restaurant.get_table(table_number)
            if item_name in table.items:
                item = table.items[item_name]
                return  item.to_dict()
        return {'message': f'Item {item_name} not found in the table {table_number}.'}, 404 

# @api.route('/restaurant')
# class RestaurantResource(Resource):

#     @app.route('/<int:table_number>/add_item', methods=['POST'])
#     @api.doc('add Item')
#     def add_item(table_number):
#         data = request.get_json()
#         item_name = data.get('item_name')
#         cook_time = random.randint(5, 15)

#         if table_number not in orders:
#             orders[table_number] = []

#         orders[table_number].append({
#             'item_name': item_name,
#             'cook_time': cook_time
#         })

#         return jsonify({'message': 'Item added to the order.'}), 201


#     @app.route('/remove_item', methods=['DELETE'])
#     def remove_item():
#         data = request.get_json()
#         table_number = data.get('table_number')
#         item_name = data.get('item_name')

#         if table_number in orders and len(orders[table_number]) > 0:
#             for item in orders[table_number]:
#                 if item['item_name'] == item_name:
#                     orders[table_number].remove(item)
#                     return jsonify({'message': 'Item removed from the order.'}), 200

#         return jsonify({'message': 'Item not found in the order.'}), 404

#     @api.doc('Get table details')
#     @api.marshal_with(table)
#     @app.route('/query_all_items/<int:table_number>', methods=['GET'])
#     def query_all_items(table_number):
#         if table_number in orders:
#             return jsonify({'items': orders[table_number]}), 200

#         return jsonify({'message': 'Table not found.'}), 404

#     @api.doc('Get table item')
#     @app.route('/query_item/<int:table_number>/<string:item_name>', methods=['GET'])
#     def query_item(table_number, item_name):
#         if table_number in orders:
#             for item in orders[table_number]:
#                 if item['item_name'] == item_name:
#                     return jsonify({'item': item}), 200

#         return jsonify({'message': 'Item not found in the order.'}), 404



# @api.route('/table/<int:table_id>')
# class TableResource(Resource):
#     @api.doc('Get table details')
#     @api.marshal_with(table)
#     def get(self, table_id):
#         """
#         Get table details
#         """
#         table = restaurant.get_table(table_id)
#         return table.__dict__

#     @api.doc('Add an item to the table')
#     @api.expect(api.model('ItemId', {'item_id': fields.Integer(required=True)}))
#     def post(self, table_id):
#         """
#         Add an item to the table
#         """
#         args = api.payload
#         item_id = args['item_id']
#         table = restaurant.get_table(table_id)
#         table.add_item(item_id)
#         return {'message': f'Item {item_id} added to table {table_id}'}

# @api.route('/item/<int:item_id>')
# class ItemResource(Resource):
#     @api.doc('Get item details')
#     @api.marshal_with(item)
#     def get(self, item_id):
#         """
#         Get item details
#         """
#         item = None
#         for table in restaurant.tables:
#             item = table.check_item(item_id)
#             if item:
#                 break
#         if item:
#             return item.__dict__
#         else:
#             return {'message': 'Item not found'}, 404

#     @api.doc('Remove an item')
#     def delete(self, item_id):
#         """
#         Remove an item
#         """
#         for table in restaurant.tables:
#             if item_id in table.items:
#                 table.remove_item(item_id)
#                 return {'message': f'Item {item_id} removed'}, 204
#         return {'message': 'Item not found'}, 404
