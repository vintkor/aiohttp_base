from .views import (
    hello_index,
)


app_name = 'index'
routes = [
    ('GET', '/', hello_index, f'{app_name}:home'),
]
