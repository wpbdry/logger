import logger
import os
import shutil

# delete old logs
if os.path.isdir('logs'):
    shutil.rmtree('logs')
os.makedirs('logs')

main = logger.Logger(
    'primary_logger',
    'logs/',
    ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
)

main.debug('This is a debug message')
main.info('This is an info message')
main.warning('This is a warning message')
main.error('This is an error message')
main.critical('This is a critical message')
