import re

def commands():
    """Returns the list of commands that this plugin handles.
    """
    return [
            {
                'type':'friends',
                'triggers':[re.compile('.*')],
                'field':'all',
            }
           ]
    
def process(status):
    return "Hello Friends!"
