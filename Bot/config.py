import logging

with open("token", "r") as file:
    API_TOKEN = file.readline()

LOGGER_LVL = logging.INFO
LOGGER_NAME_OF_FILE_LOG = "log.log"