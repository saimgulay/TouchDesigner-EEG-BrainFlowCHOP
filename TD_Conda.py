import sys
import os
import platform

def onStart():
    # 1. SETUP PATHS
    # Note: We are using the '.conda' path you found earlier
    user = 'username'
    conda_base = f'C:/Users/{user}/.conda/envs/TD'
    
    # 2. DEFINE SUB-FOLDERS
    dll_path = os.path.join(conda_base, 'DLLs')
    bin_path = os.path.join(conda_base, 'Library', 'bin')
    site_packages = os.path.join(conda_base, 'Lib', 'site-packages')

    if platform.system().lower() == 'windows':
        # 3. CHECK IF ENVIRONMENT EXISTS
        if not os.path.exists(conda_base):
            print(f"CRITICAL ERROR: Path not found: {conda_base}")
            return

        # 4. ADD DLLs (Critical for NumPy to work)
        # We try/except this because on some Python versions this function doesn't exist
        try:
            if os.path.exists(dll_path):
                os.add_dll_directory(dll_path)
            if os.path.exists(bin_path):
                os.add_dll_directory(bin_path)
        except AttributeError:
            # Fallback for older Python or different configs
            os.environ['PATH'] = dll_path + os.pathsep + os.environ['PATH']
            os.environ['PATH'] = bin_path + os.pathsep + os.environ['PATH']

        # 5. INSERT SITE-PACKAGES (THE MOST IMPORTANT PART)
        # We use insert(0) to force Conda libraries to load BEFORE TouchDesigner libraries
        # This should fix the 'numpy.exceptions' error.
        if site_packages not in sys.path:
            sys.path.insert(0, site_packages)
            print(f"SUCCESS: Conda Loaded. Path added: {site_packages}")
        
    return
