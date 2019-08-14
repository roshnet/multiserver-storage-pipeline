import falcon
from resources import Storage

api = falcon.API()

api.add_route('/storage/{filename}', Storage())