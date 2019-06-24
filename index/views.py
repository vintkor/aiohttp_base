from aiohttp_jinja2 import template


@template('base.html')
async def hello_index(request):
    context = dict()
    return context
