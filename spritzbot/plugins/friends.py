def commands():
    """Returns the list of commands that this plugin handles.
    """
    return [
            {'type':'friends',
             'triggers':['.*']}
           ]
    
def process(command, arguments):
    return "Hello World!"