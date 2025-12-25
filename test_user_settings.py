#!/usr/bin/env python3
# =========================================================
#  USER SETTINGS TEST — SupraZone v3.3
#  Purpose: Test user settings functionality
# =========================================================

import sys
import os

# Add suprazone directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'suprazone'))

from user_settings import (
    load_user_settings, 
    save_user_settings, 
    get_user_info,
    DEFAULT_SETTINGS
)

def test_load_default_settings():
    """Test loading default settings."""
    print("Test 1: Loading default settings...")
    settings = load_user_settings()
    assert 'author' in settings, "Settings should contain 'author' key"
    assert 'email' in settings, "Settings should contain 'email' key"
    assert 'organization' in settings, "Settings should contain 'organization' key"
    print("  ✅ Default settings loaded successfully")
    return True

def test_save_and_load_settings():
    """Test saving and loading custom settings."""
    print("\nTest 2: Saving and loading custom settings...")
    
    test_settings = {
        'author': 'Test User',
        'email': 'test@example.com',
        'organization': 'Test Org'
    }
    
    # Save test settings
    success = save_user_settings(test_settings)
    assert success, "Settings should be saved successfully"
    
    # Load and verify
    loaded_settings = load_user_settings()
    assert loaded_settings['author'] == 'Test User', "Author should match"
    assert loaded_settings['email'] == 'test@example.com', "Email should match"
    assert loaded_settings['organization'] == 'Test Org', "Organization should match"
    
    print("  ✅ Custom settings saved and loaded successfully")
    return True

def test_get_user_info():
    """Test get_user_info function."""
    print("\nTest 3: Getting user info...")
    user_info = get_user_info()
    assert isinstance(user_info, dict), "User info should be a dictionary"
    assert 'author' in user_info, "User info should contain 'author'"
    assert 'email' in user_info, "User info should contain 'email'"
    print("  ✅ User info retrieved successfully")
    return True

def restore_original_settings():
    """Restore original settings."""
    print("\nRestoring original settings...")
    save_user_settings(DEFAULT_SETTINGS)
    print("  ✅ Original settings restored")

def main():
    """Run all tests."""
    print("=" * 60)
    print("  SupraZone Framework — User Settings Tests")
    print("=" * 60)
    
    try:
        test_load_default_settings()
        test_save_and_load_settings()
        test_get_user_info()
        restore_original_settings()
        
        print("\n" + "=" * 60)
        print("  ✅ All tests passed!")
        print("=" * 60)
        return 0
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        restore_original_settings()
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        restore_original_settings()
        return 1

if __name__ == "__main__":
    sys.exit(main())
