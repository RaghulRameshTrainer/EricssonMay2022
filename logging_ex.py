import logging
'''
5 built in level
DEBUG    10
INFO     20
WARNING  30
ERROR    40
CRITICAL 50
'''
LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="output.log",level=logging.DEBUG,format=LOG_FORMAT,
                    filemode='a')
logger=logging.getLogger()
logger.debug("Job has run longer")
logger.info("Job has run longer")
logger.warning("Job has run longer")
logger.error("Job been terminated")
logger.critical("Job has been failed")

