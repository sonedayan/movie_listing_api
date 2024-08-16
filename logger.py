import logging
from logging.handlers import SysLogHandler
from dotenv import load_dotenv
import os

load_dotenv()

# Load environment variables
PAPERTRAIL_HOST = os.environ.get("PAPERTRAIL_HOST")
PAPERTRAIL_PORT = int(os.environ.get("PAPERTRAIL_PORT"))

# Configure the logger
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logger.setLevel(logging.INFO)

# Set up the Papertrail handler
handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

print(f"PAPERTRAIL_HOST: {PAPERTRAIL_HOST}, PAPERTRAIL_PORT: {PAPERTRAIL_PORT}")

