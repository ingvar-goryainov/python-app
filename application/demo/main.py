from argparse import ArgumentParser

from aiohttp import web

from .web_app import init_app
from .logger import logger


def build_parser_args(cli_args=None):
    parser = build_parser()
    return parser.parse_args(args=cli_args)


def build_parser(args=None):
    parser = ArgumentParser(
        allow_abbrev=False,
        description="It's just a test python application",
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8080,
    )

    return parser


def _run_app(namespace):
    app = init_app()
    web.run_app(
        app,
        port=int(namespace.port)
    )


def main(cli_args=None):
    logger.info("Starting app")
    namespace = build_parser_args(cli_args)
    _run_app(namespace)


if __name__ == '__main__':
    main()
