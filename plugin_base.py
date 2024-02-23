# plugin_base.py
class PluginBase:
    def execute(self):
        raise NotImplementedError("Each plugin must implement the 'execute' method.")
