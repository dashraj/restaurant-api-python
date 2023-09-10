from server.instance import server

# Need to import all resources
from controllers.restaurantController import *

if __name__ == '__main__':
    server.run()