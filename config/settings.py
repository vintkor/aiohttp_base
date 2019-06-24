import os
from pathlib import Path

BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'templates'))
APP_ROOT_DIR = Path(__file__).parents[1]

DEBUG = True

APP_LIST = [
    'index',
    'blog',
]
