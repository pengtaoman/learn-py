import falcon
import json
from wsgiref.simple_server import make_server

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': 'I\'ve always been more interested in '
                     'the future than in the past.',
            'author': 'Grace Hopper'
        }
        resp.body = json.dumps(quote)


api = falcon.App()
api.add_route('/quote', QuoteResource())


if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()
