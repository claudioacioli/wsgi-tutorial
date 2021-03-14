#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
from util import get_template


def application (environ, start_response):

    # PEP 3333 says: CONTENT_LENGTH may be empty or missing
    try:
        request_content_length = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_content_length = 0

    # Request Body is passed inside wsgi.input environment variable
    request_body = environ['wsgi.input'].read(request_content_length)
    form = parse_qs(request_body.decode('utf-8'))

    age = form.get('age', [''])[0]
    hobbies = form.get('hobbies', [])

    age = escape(age)
    hobbies = [escape(hobby) for hobby in hobbies]

    html = get_template('template.html')
    body = html % {
            'method': 'POST',
            'checked-software': ('', 'checked')['software' in hobbies],
            'checked-tunning': ('', 'checked')['tunning' in hobbies],
            'age': age or 'Empty',
            'hobbies': ', '.join(hobbies or ['No Hobbies?'])
        }

    status = '200 OK'

    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Lenght', str(len(body)))
    ]

    start_response(status, headers)
    return [bytes(body, 'utf-8')]


if __name__ == '__main__':
    httpd = make_server('0.0.0.0', 8051, application)
    httpd.serve_forever()
