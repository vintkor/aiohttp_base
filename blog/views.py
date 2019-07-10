from aiohttp import web
from aiohttp_jinja2 import template
from .models import Post
from tortoise import exceptions as te


@template('blog/blog_list.html')
async def post_list(request):
    posts = await Post.all()
    context = {'posts': posts}
    return context


@template('blog/blog_detail.html')
async def post_detail(request):
    post_id = request.match_info['id']
    try:
        post = await Post.get(id=post_id)
    except te.DoesNotExist:
        return web.HTTPNotFound()
    context = {'post': post}
    return context


async def post_list_as_JSON(request):
    if request.method == 'GET':
        posts = await Post.all()
        context = []
        to_serialize = ['id', 'title']
        for post in posts:
            context.append(post.to_json(to_serialize))
        return web.json_response(context)
    return web.HTTPNotFound()
