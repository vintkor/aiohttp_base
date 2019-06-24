from .views import (
    post_list,
)


app_name = 'blog'
routes = [
    ('GET', f'/{app_name}', post_list, f'{app_name}:post-list'),
]
