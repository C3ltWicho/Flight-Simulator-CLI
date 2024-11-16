import logging
from logging import handlers

def setup_logging(loglevel="INFO"):
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {loglevel}' )
    logging.basicConfig(
        filename="logTest.log", 
        encoding='utf-8',
        format='%(asctime)s - %(levelname)s - %(message)s' ,
        level=numeric_level
    )
    logger = logging.getLogger(__name__)
    return logger
    #logging.warning('is when this even was logged.')