import os

import aiohttp
import pkg_resources
from aiohttp import web

VERSION = str(pkg_resources.require("demo")[0].version)
HOSTNAME = os.environ.get('HOSTNAME')
EXTERNAL_URL = os.environ.get('EXTERNAL')


async def health(request: web.Request):
    return web.json_response({"status": "OK"})


async def app_info(request: web.Request):
    return web.Response(
        body="Hostname: {}. Version: {}".format(
            HOSTNAME,
            VERSION,
        )
    )


async def external_get(request: web.Request):
    if not EXTERNAL_URL:
        return web.Response(
            body="{}: External url isn't defined".format(HOSTNAME),
            status=500,
        )
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(EXTERNAL_URL) as resp:
                return web.Response(
                    body=await resp.text(),
                    status=resp.status,
                    content_type=resp.content_type,
                )
    except BaseException as err:
        return web.Response(
            body=str(err),
            status=503,
        )


async def get_request_headers(request: web.Request):
    return web.json_response(
        {
            "request_headers": dict(request.headers),
        },
        status=200,
    )


async def get_request_info(request: web.Request):
    return web.json_response(
        {
            "headers": dict(request.headers),
            "body": await request.text(),
        },
        status=200,
    )