from aiohttp import web
from .views import health, external_get, app_info, get_request_headers, get_request_info


def setup_routes(app: web.Application):
    app.router.add_route("GET", "/", app_info)
    app.router.add_route("GET", "/health", health)
    app.router.add_route("GET", "/external", external_get)
    app.router.add_route("GET", "/headers", get_request_headers)
    app.router.add_route("POST", "/request", get_request_info)
