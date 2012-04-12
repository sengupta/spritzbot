import os
import re
import imp
import json

class TweetProcessor:
    plugins = {}
    commands = {}
    base_path = os.path.dirname(os.path.realpath(__file__))
    plugin_path = os.path.join(base_path, "plugins")

    def __init__(self):
        self.load_plugins()
    
    def load_plugins(self):
        """Loads plugins and associated commands."""
        # Filename pattern that we want to load.
        re_plugin = re.compile('[^.].*\.py$')
        
        for plugin_module in os.listdir(self.plugin_path):
            if re_plugin.match(plugin_module):
                # Get the module's name
                name = plugin_module[:-3]
                plugin_info = imp.find_module(name, [self.plugin_path])
                plugin = imp.load_module(name, *plugin_info)
                self.plugins.update({name:plugin})
                
                for command in plugin.commands():
                    status_type = command['type']
                    triggers = command['triggers']
                    if self.commands.has_key(status_type):
                        self.commands[status_type].append({'plugin':name,'triggers':triggers})
                    else:
                        self.commands[status_type] = [{'plugin':name,'triggers':triggers}]
    

    def process(self, data):
        """Processes the status/tweet and hands over to appropriate plugins."""
        try:
            status = json.loads(data)
        except:
            return None
        
        for status_type in self.commands:
            # see if it is of typs 'text' or 'friends' or something else
            if status.has_key(status_type):
                # if it is, find out the modules associated with it
                commands = self.commands[status_type]
                # for each module that handles say 'text', 
                for command in commands:
                    # for triggers that should send data to process
                    # in that module,
                    triggers = command['triggers']
                    for t in triggers:
                        # compiled regex match:
                        if t.match(data):
                            # currently, we're just printing the output
                            # later there will be facility to reply
                            # or better - send a tweepy api object to the
                            # processing module so it can take actions
                            # independently.
                            print self.plugins[command['plugin']].process(status)


if __name__ == '__main__':
    tp = TweetProcessor()
    
    tweet = r"""{"text":"Chai craving!","id":190207791800135680}"""
    friends = r"""{"friends":[123,456,789]}"""
    
    tp.process(friends)
    tp.process(tweet)
