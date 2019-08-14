import falcon


class Storage(object):

    # Handle data in POST requests
    def on_post(self, req, resp, filename):
        if "/" in filename:
            resp.status = falcon.HTTP_400
        content = req.stream.read()
        with open(filename, 'wb') as fw:
            fw.write(content)
        print("[+] File written")