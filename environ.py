from wsgiref.simple_server import make_server


def application(environ, start_response):
    status = '200 OK'
    body = ['<tr><td>{}</td><td>{}</td></tr>'.format(key, value) for key, value in sorted(environ.items())]
    body = '\n'.join(body)
    body = '<table border="1">{}</table>'.format(body)
    lenght = str(len(body))
    headers = ([
        ('Content-Type', 'text/html'),
        ('Content-Lenght', lenght)
    ])
    start_response(status, headers)
    return [bytes(body, 'utf-8')]


httpd = make_server('0.0.0.0', 8080, application)
httpd.handle_request()
