import logging
import os
from datetime import datetime

# creating a file name formate to store a logs based on the date and time
log_path_name=f'{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log'
log_folder=f'{datetime.now().strftime('%d_%m_%Y')}.log'

# joining the path of current directory, log file folder with date and time
log_path=os.path.join(os.getcwd(),'logs',log_folder)

os.makedirs(log_path, exist_ok=True)

entire_logfile_path=os.path.join(log_path,log_path_name)

logging.basicConfig(
    filename=entire_logfile_path,
    format='[%(asctime)s] line: %(lineno)s filename = %(filename)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__=="__main__":
    logging.info('logging started')