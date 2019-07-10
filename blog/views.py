from aiohttp_jinja2 import template
from .models import Post


@template('blog/blog_list.html')
async def post_list(request):
    posts = await Post.all()
    context = {'posts': posts}
    return context


@template('blog/blog_detail.html')
async def post_detail(request):
    post_id = request.match_info['id']
    post = await Post.get(id=post_id)
    context = {'post': post}
    return context
