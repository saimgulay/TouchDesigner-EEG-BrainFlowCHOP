import sys
import os
import platform

def onStart():
    print("------------------------------------------------")
    print("DEBUG: Starting Script...")

    # --- PATH CONFIGURATION ---
    # Using the correct path you found:
    base_path = 'C:/Users/username/.conda/envs/env_Name'
    # --------------------------

    if platform.system().lower() == 'windows':
        dll_path = base_path + '/DLLs'
        bin_path = base_path + '/Library/bin'
        site_packages = base_path + '/Lib/site-packages'

        # 1. Add DLLs (Crucial for Windows)
        if sys.version_info.major >= 3 and sys.version_info.minor >= 8:
            if os.path.isdir(dll_path):
                os.add_dll_directory(dll_path)
            if os.path.isdir(bin_path):
                os.add_dll_directory(bin_path)
        else:
            os.environ['PATH'] = dll_path + os.pathsep + bin_path + os.pathsep + os.environ['PATH']

        # 2. Add Site-Packages (Libraries)
        # We use insert(0) to ensure Conda paths are FIRST in the list
        if os.path.exists(site_packages):
            if site_packages not in sys.path:
                sys.path.insert(0, site_packages)
                print(f"SUCCESS: Added site-packages: {site_packages}")
        else:
            print(f"CRITICAL ERROR: Could not find site-packages at {site_packages}")
            return

    # --- THE FIX FOR NUMPY ERROR ---
    # Force Python to reload NumPy from your Conda env instead of TD's built-in one.
    
    try:
        import numpy
        # Check if the loaded numpy is the old one (from TouchDesigner folder)
        # If the path doesn't contain 'envs', it's likely the wrong one.
        if 'envs' not in numpy.__file__:
            print("WARNING: Default TouchDesigner NumPy is loaded. Attempting to swap...")
            
            # Remove numpy from memory
            if 'numpy' in sys.modules:
                del sys.modules['numpy']
            if 'numpy.core' in sys.modules:
                del sys.modules['numpy.core']
            
            # Re-import to grab the one from Conda (since we added it to sys.path[0])
            import numpy
            print(f"SUCCESS: Swapped to Conda NumPy version: {numpy.__version__}")
        else:
            print(f"SUCCESS: Correct NumPy already loaded: {numpy.__version__}")
            
    except Exception as e:
        print(f"ERROR: Could not swap NumPy. Reason: {e}")

    print("------------------------------------------------")
    return
