import os
import re
import imp

PLUGINS = {}
COMMANDS = {}
BASE_PATH = os.path.dirname(os.path.realpath(__file__))
PLUGIN_PATH = os.path.join(BASE_PATH, "plugins")

def load_plugins():
    """Loads all plugins and the associated commands.
    Code borrowed from gtalkbot.py
    """
    global PLUGINS, COMMANDS, PLUGIN_PATH
    re_plugin = re.compile('[^.].*\.py$')
    loaded_plugins = []
    for plugin_file in os.listdir(PLUGIN_PATH):
        if re_plugin.match(plugin_file):
            name = plugin_file[:-3]
            plugin_info = imp.find_module(name, [PLUGIN_PATH])
            plugin = imp.load_module(name, *plugin_info)
            PLUGINS[name] = plugin
            loaded_plugins.append(name)
            # Load the commands supported by this plugin
            for command in plugin.commands():
                COMMANDS.update({name:command})

    return loaded_plugins

print load_plugins()
print COMMANDS
print PLUGINS