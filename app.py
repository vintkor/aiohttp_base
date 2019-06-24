import aiohttp_jinja2
import jinja2
from aiohttp import web
from config import settings
import aiohttp_debugtoolbar
import asyncio
import uvloop
from config import url_helper


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = web.Application()
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(settings.TEMPLATE_DIR),
    context_processors=[aiohttp_jinja2.request_processor],
)

if settings.DEBUG:
    aiohttp_debugtoolbar.setup(app, intercept_redirects=False)

for route in url_helper.routes:
    app.router.add_route(route[0], route[1], route[2], name=route[3])

if __name__ == '__main__':
    web.run_app(app)
