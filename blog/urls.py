from .views import (
    post_list,
    post_detail,
    post_list_as_JSON,
)


app_name = 'blog'
routes = [
    ('GET', f'/{app_name}/', post_list, f'{app_name}:post-list'),
    ('GET', f'/{app_name}/api/', post_list_as_JSON, f'{app_name}:post-list-api'),
    ('GET', f'/{app_name}/' + '{id:\d+}', post_detail, f'{app_name}:post-detail'),
]
