from wsgiref.simple_server import make_server


def application(environ, start_response):
    response_body = 'Request method: %s\n' % environ['REQUEST_METHOD']
    status = '200 OK'
	
    response_headers = [
        ('Content-type', 'text/plain'),
	('Content-Lenght', str(len(response_body)))
    ]

    start_response(status, response_headers)

    return [bytes(response_body, 'utf-8')]


httpd = make_server('localhost', 8080, application)
httpd.handle_request()
