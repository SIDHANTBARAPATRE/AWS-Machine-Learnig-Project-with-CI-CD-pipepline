import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # creating logfile name.
logs_path=os.path.join(os.getcwd(),"logs") # creating logs folder path
os.makedirs(logs_path,exist_ok=True) # making logs directory

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) # creating log file inside logs folder.

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

# if __name__ == "__main__":
#     logging.info("logging started") # uncomment and check python logger.py to see whether working or not.


