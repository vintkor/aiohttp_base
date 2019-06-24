import os
from . import settings
import importlib


routes = []
for folder in os.listdir(settings.APP_ROOT_DIR):
    if folder in settings.APP_LIST:
        try:
            routes += importlib.import_module(f'{folder}.urls').routes
        except ModuleNotFoundError:
            pass
