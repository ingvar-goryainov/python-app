import logging

logging.basicConfig(
    format="%(asctime)-20s %(levelname)5s :: %(name)s :: %(module)s.%(funcName)s :: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
