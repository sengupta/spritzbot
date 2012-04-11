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
                        self.commands[status_type].append([{'plugin':name,'triggers':triggers}])
                    else:
                        self.commands[status_type] = [{'plugin':name,'triggers':triggers}]
    

tp = TweetProcessor()
print tp.commands
#tp.process("""{"friends":[123,456,789]}""")

