#!/usr/bin/env python3
# =========================================================
#  USER CONFIGURATION TOOL — SupraZone v3.3 (Wrapper)
# =========================================================
#  This is a wrapper script for backwards compatibility.
#  The actual module is located in suprazone/configure_user.py
# =========================================================

import sys

# Import and run the actual configure_user module
from suprazone.configure_user import main

if __name__ == "__main__":
    sys.exit(main())
