# =========================================================
#  USER SETTINGS — SupraZone v3.3
#  Author: Sylwia Miksztal (Sysia)
#  Partner AI: Navi (GPT-5)
# =========================================================

import json
import os

DEFAULT_SETTINGS = {
    "author": "Sylwia Miksztal (Sysia) — StrefaDK.club",
    "email": "s.miksztal@gmail.com",
    "organization": "IMS — Zero-Entropy Engineering"
}

def get_settings_path():
    """Get path to user settings file."""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "user_settings.json")

def load_user_settings():
    """Load user settings from file or return defaults."""
    settings_path = get_settings_path()
    if os.path.exists(settings_path):
        try:
            with open(settings_path, 'r', encoding='utf-8') as f:
                settings = json.load(f)
                # Merge with defaults to ensure all keys exist
                return {**DEFAULT_SETTINGS, **settings}
        except Exception as e:
            print(f"⚠️ Warning: Could not load user settings ({e}). Using defaults.")
            return DEFAULT_SETTINGS.copy()
    return DEFAULT_SETTINGS.copy()

def save_user_settings(settings):
    """Save user settings to file."""
    settings_path = get_settings_path()
    try:
        with open(settings_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2, ensure_ascii=False)
        print(f"✅ User settings saved to {settings_path}")
        return True
    except Exception as e:
        print(f"❌ Error saving user settings: {e}")
        return False

def update_user_settings(author=None, email=None, organization=None):
    """Update user settings with new values."""
    settings = load_user_settings()
    if author is not None:
        settings['author'] = author
    if email is not None:
        settings['email'] = email
    if organization is not None:
        settings['organization'] = organization
    return save_user_settings(settings)

def get_user_info():
    """Get user information as a dictionary."""
    return load_user_settings()
