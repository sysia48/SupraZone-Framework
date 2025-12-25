#!/usr/bin/env python3
# =========================================================
#  USER CONFIGURATION TOOL — SupraZone v3.3
#  Author: Sylwia Miksztal (Sysia)
#  Partner AI: Navi (GPT-5)
# =========================================================
#  Purpose: Configure user account settings for SupraZone
# =========================================================

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from user_settings import load_user_settings, save_user_settings, get_user_info

def main():
    """Interactive user settings configuration."""
    print("=" * 60)
    print("  SupraZone Framework — User Account Settings")
    print("=" * 60)
    print()
    
    # Load current settings
    current_settings = load_user_settings()
    
    print("Current settings:")
    print(f"  Author: {current_settings.get('author', 'Not set')}")
    print(f"  Email: {current_settings.get('email', 'Not set')}")
    print(f"  Organization: {current_settings.get('organization', 'Not set')}")
    print()
    
    # Ask if user wants to update
    update = input("Would you like to update these settings? (y/n): ").strip().lower()
    
    if update != 'y':
        print("No changes made.")
        return
    
    print("\nEnter new values (press Enter to keep current value):")
    print()
    
    # Get new author name
    author = input(f"Author [{current_settings.get('author', '')}]: ").strip()
    if not author:
        author = current_settings.get('author', '')
    
    # Get new email
    email = input(f"Email [{current_settings.get('email', '')}]: ").strip()
    if not email:
        email = current_settings.get('email', '')
    
    # Get new organization
    organization = input(f"Organization [{current_settings.get('organization', '')}]: ").strip()
    if not organization:
        organization = current_settings.get('organization', '')
    
    # Save new settings
    new_settings = {
        'author': author,
        'email': email,
        'organization': organization
    }
    
    if save_user_settings(new_settings):
        print()
        print("=" * 60)
        print("✅ Settings updated successfully!")
        print("=" * 60)
        print()
        print("New settings:")
        print(f"  Author: {new_settings['author']}")
        print(f"  Email: {new_settings['email']}")
        print(f"  Organization: {new_settings['organization']}")
    else:
        print("❌ Failed to save settings.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
