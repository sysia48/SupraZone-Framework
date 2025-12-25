#!/usr/bin/env python3
# =========================================================
#  USER SETTINGS EXAMPLE — SupraZone v3.3
#  Purpose: Demonstrate user settings functionality
# =========================================================

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from user_settings import get_user_info, update_user_settings, load_user_settings

def example_get_user_info():
    """Example: Get current user information."""
    print("=" * 60)
    print("Example 1: Get User Information")
    print("=" * 60)
    
    user_info = get_user_info()
    print(f"\nCurrent User Information:")
    print(f"  Author:       {user_info['author']}")
    print(f"  Email:        {user_info['email']}")
    print(f"  Organization: {user_info['organization']}")
    print()

def example_update_settings():
    """Example: Update user settings programmatically."""
    print("=" * 60)
    print("Example 2: Update User Settings")
    print("=" * 60)
    
    print("\nUpdating settings...")
    success = update_user_settings(
        author="Example User",
        email="example@domain.com",
        organization="Example Org"
    )
    
    if success:
        print("✅ Settings updated successfully!")
        
        # Load and display updated settings
        user_info = load_user_settings()
        print(f"\nUpdated User Information:")
        print(f"  Author:       {user_info['author']}")
        print(f"  Email:        {user_info['email']}")
        print(f"  Organization: {user_info['organization']}")
    else:
        print("❌ Failed to update settings")
    print()

def example_restore_defaults():
    """Example: Restore default settings."""
    print("=" * 60)
    print("Example 3: Restore Default Settings")
    print("=" * 60)
    
    from user_settings import DEFAULT_SETTINGS, save_user_settings
    
    print("\nRestoring default settings...")
    success = save_user_settings(DEFAULT_SETTINGS)
    
    if success:
        print("✅ Default settings restored!")
        user_info = load_user_settings()
        print(f"\nRestored User Information:")
        print(f"  Author:       {user_info['author']}")
        print(f"  Email:        {user_info['email']}")
        print(f"  Organization: {user_info['organization']}")
    else:
        print("❌ Failed to restore defaults")
    print()

def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("  SupraZone Framework — User Settings Examples")
    print("=" * 60)
    print()
    
    # Example 1: Get current user information
    example_get_user_info()
    
    # Example 2: Update settings
    example_update_settings()
    
    # Example 3: Restore defaults
    example_restore_defaults()
    
    print("=" * 60)
    print("  Examples completed!")
    print("=" * 60)
    print("\nFor interactive configuration, run:")
    print("  python configure_user.py")
    print()

if __name__ == "__main__":
    main()
