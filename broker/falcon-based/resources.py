import falcon
import os

STORAGE_FOLDER = 'storage'


class Storage(object):
    def on_post(self, req, resp, filename):
        if "/" in filename:
            resp.status = falcon.HTTP_400
            resp.body = "Cannot contain sub directories"

        filepath = os.path.join(STORAGE_FOLDER, filename)
        with open(filepath, 'wb') as fp:
            fp.write(req.stream.read())
