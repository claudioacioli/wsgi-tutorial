#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<!DOCTYPE html>
<html>
  <body>
    <form method="GET" action="">
      <p>
        Age: <input type="text" name="age" value="%(age)s">
      </p>
      <p>
        Hobbies:
        <label>
          <input name="hobbies" type="checkbox" value="software" %(checked-software)s>
          Software
        </label>
        <label>
          <input name="hobbies" type="checkbox" value="tunning" %(checked-tunning)s>
          Auto tunning
        </label>
      </p>
      <p>
        <input type="submit" value="submit">
      </p>
    </form>
    <p>
      Age: %(age)s<br>
      Hobbies: %(hobbies)s
    </p>
  </body>
</html>
"""

def application (environ, start_response):

    # translate ENVIRON variable about query string to dict
    query = parse_qs(environ['QUERY_STRING'])

    # As there can ben more than one value for a variable then
    # a list is provied as a default for parse_qs
    age = query.get('age', [''])[0]
    hobbies = query.get('hobbies', [])

    body = html % {
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
