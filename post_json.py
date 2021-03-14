from wsgiref.simple_server import make_server
import json

def get_request_length(environ):
    try:
        return int(environ['CONTENT_LENGTH'] or 0)
    except ValueError:
        return 0


def get_request_body(environ):
    length = get_request_length(environ)
    if length:
        body = environ['wsgi.input'].read(length)
        return body.decode('utf-8')
    
    return None


def handle_request_json(environ):
    try:
        body = get_request_body(environ) or '{}'
        return json.loads(body)
    except:
        return {}


def application (environ, start_response):
    status = '200 OK'
    body = 'Alo mundo'
   
    method = environ['REQUEST_METHOD']
    if method == 'POST' and environ['CONTENT_TYPE'] == 'application/json':
        json_params = handle_request_json(environ)
        print(json_params)

    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]

    start_response(
        status,
        headers
    )
    
    return [bytes(body, 'utf-8')]


if __name__ == '__main__':
    server = make_server('0.0.0.0', 8080,  application)
    server.serve_forever()
