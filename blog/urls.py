from .views import (
    post_list,
    post_detail,
)


app_name = 'blog'
routes = [
    ('GET', f'/{app_name}/', post_list, f'{app_name}:post-list'),
    ('GET', f'/{app_name}/' + '{id}', post_detail, f'{app_name}:post-detail'),
]
