import importlib
import os

from plugin_base import PluginBase


# 动态加载并执行插件
def load_and_execute_plugins(plugin_dir):
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            # 从文件名中去掉.py后缀并导入模块
            module_name = filename[:-3]
            module = importlib.import_module(f"{plugin_dir}.{module_name}")

            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if isinstance(attribute, type) and issubclass(attribute, PluginBase) and attribute is not PluginBase:
                    # 实例化插件并执行
                    plugin_instance = attribute()
                    print(plugin_instance.execute())


# 假设插件存放在当前目录下的"plugins"文件夹中
load_and_execute_plugins("plugins")
