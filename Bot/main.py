import aiogram
import logging
import config


logging.basicConfig(
    level=config.LOGGER_LVL,
    handlers=[
        logging.FileHandler(config.LOGGER_NAME_OF_FILE_LOG),
        logging.StreamHandler(),
    ],
    format='[%(asctime)s] - [%(name)s] - [%(levelname)s] - %(message)s',
)

logger = logging.getLogger(__name__)


