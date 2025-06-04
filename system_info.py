import platform
from datetime import datetime

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log_message(self, message):
        print(message)
        with open(self.log_file, "a") as f:
            f.write(message + "\n")

def get_system_info(logger):
    logger.log_message("---- System Information ----")
    logger.log_message(f"System      : {platform.system()}")
    logger.log_message(f"Node Name   : {platform.node()}")
    logger.log_message(f"Release     : {platform.release()}")
    logger.log_message(f"Version     : {platform.version()}")
    logger.log_message(f"Machine     : {platform.machine()}")
    logger.log_message(f"Processor   : {platform.processor()}")
    logger.log_message("----------------------------")

def log_current_time(logger):
    now = datetime.now()
    logger.log_message(f"Current Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    now = datetime.now()
    log_file = f"output_{now.strftime('%Y%m%d_%H%M%S')}.log"
    
    logger = Logger(log_file)
    
    get_system_info(logger)
    log_current_time(logger)
