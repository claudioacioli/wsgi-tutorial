

def get_template(name):
    template = ''
    with open(name, 'r') as file:
        template = file.read()
    return template
