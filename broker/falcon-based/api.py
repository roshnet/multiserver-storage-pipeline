import falcon


class Resource(object):

    def on_post(self, req, resp):
        in_file = req.get_param('file')
        
