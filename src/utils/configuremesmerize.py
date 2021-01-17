import sys
import re
import pathlib
import logging
from typing import Dict, Union, Optional, Any

setup_log = logging.getLogger("mesmerize.setup")

config_dir = None
