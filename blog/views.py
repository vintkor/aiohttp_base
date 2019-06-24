from aiohttp_jinja2 import template


@template('blog/blog_list.html')
async def post_list(request):
    posts = [
        {'title': 'post 1'},
        {'title': 'post 2'},
        {'title': 'post 3'},
    ]
    context = {
        'posts': posts,
    }
    return context
