from flask import Flask
from flask_restx import Api
from environment.instance import environment_config

class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app, 
            version='1.0', 
            title='Restaurant API',
            description='Restaurant management API', 
            doc = environment_config["swagger-url"]
        )

    def run(self):
        self.app.run(
                debug = environment_config["debug"], 
                port = environment_config["port"]
            )

server = Server()