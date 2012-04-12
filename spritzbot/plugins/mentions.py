import re

def commands():
    """Returns the list of commands that this plugin handles.
    """
    return [
            {
                'type':'text',
                'triggers':[re.compile('.*')],
                'field':'text'
            }
           ]
    
def process(data):
    return "Hello World!"