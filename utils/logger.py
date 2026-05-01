import logging
from utils.config import settings

def setup_logger():
    logger = logging.getLogger("audit_pipelinne")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger
    

    # File Handler
    file_handler = logging.FileHandler(settings.log_file)
    file_handler.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Format
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
