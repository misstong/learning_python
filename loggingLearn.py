import logging

"""
basicConfig:设置level，filename，format...
fivel levels
"""
logging.basicConfig(level=logging.DEBUG,filename='app.log',filemode='w',format='%(name)s - %(levelname)s - %(message)s')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

"""
getLogger
"""
logger = logging.getLogger('example_logger')
# logger.basicConfig(format='%(level)s:%(name):%(message)') custom logger doesn't have basicConfig
logger.warning('This is a warning')


logger = logging.getLogger(__name__)#use built-in variable

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.ERROR)

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.debug('This is a warning')
logger.error('This is an error')