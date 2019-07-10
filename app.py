import aiohttp_jinja2
import jinja2
from aiohttp import web
from config import settings
import aiohttp_debugtoolbar
import asyncio
import uvloop
from config import url_helper
from tortoise import Tortoise
from config.db_services import DBAsyncClient
from run_migrations import run_migrations


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()


async def init_db():
    await Tortoise.init(settings.TORTOISE_CONFIG)
    await Tortoise.generate_schemas()


async def create_app():
    app = web.Application()
    app['db'] = DBAsyncClient(**settings.DB_CONFIG)
    loop.create_task(init_db())
    loop.create_task(run_migrations())

    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(settings.TEMPLATE_DIR),
        context_processors=[aiohttp_jinja2.request_processor],
    )

    if settings.DEBUG:
        aiohttp_debugtoolbar.setup(app, intercept_redirects=False)

    for route in url_helper.routes:
        app.router.add_route(route[0], route[1], route[2], name=route[3])

    return app


if __name__ == '__main__':
    create_app()
