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

DB_CONFIG = {
    'user': 'aiohttp_test',
    'password': 'aiohttp_test',
    'database': 'aiohttp_test',
    'host': 'localhost',
    'port': '5432',
    'connections': '',
    'connection_name': '',
}


TORTOISE_CONFIG = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': DB_CONFIG['host'],
                'port': DB_CONFIG['port'],
                'user': DB_CONFIG['user'],
                'password': DB_CONFIG['password'],
                'database': DB_CONFIG['database'],
            }
        },
    },
    'apps': {
        'models': {
            'models': ['blog.models'],
            # If no default_connection specified, defaults to 'default'
            'default_connection': 'default',
        }
    }
}
