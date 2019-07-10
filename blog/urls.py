from .views import (
    post_list,
    post_detail,
)


app_name = 'blog'
routes = [
    ('GET', '/' + app_name, post_list, f'{app_name}:post-list'),
    ('GET', '/' + app_name + '/{id}', post_detail, f'{app_name}:post-detail'),
]
