import logging
#logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.DEBUG)
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M%S',
    level=logging.DEBUG,
    filename='log.txt'
)
logger = logging.getLogger('__name__')
logger.info('This will not show')
logger.warning('This will show')
logger.debug('This is debug')
logger.critical('This is critical')
"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""