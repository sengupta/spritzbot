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
    
def process(event):
    return "You have %s friends." %(len(event['friends']))
