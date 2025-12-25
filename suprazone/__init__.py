# SupraZone Framework Package
# Makes the suprazone directory importable as a package

__version__ = "3.3.0"
__author__ = "Sylwia Miksztal (Sysia)"
__email__ = "s.miksztal@gmail.com"

# Import main components for easy access
from .user_settings import (
    get_user_info,
    load_user_settings,
    save_user_settings,
    update_user_settings,
    DEFAULT_SETTINGS
)

from .configure_user import main as configure_user_main

__all__ = [
    'get_user_info',
    'load_user_settings',
    'save_user_settings',
    'update_user_settings',
    'DEFAULT_SETTINGS',
    'configure_user_main'
]
