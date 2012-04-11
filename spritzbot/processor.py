import os
import re
import imp

class TweetProcessor:
    plugins = {}
    commands = []
    base_path = os.path.dirname(os.path.realpath(__file__))
    plugin_path = os.path.join(base_path, "plugins")
    
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
                    self.commands.append({name:command})
    

tp = TweetProcessor()
tp.load_plugins()
print tp.commands
        