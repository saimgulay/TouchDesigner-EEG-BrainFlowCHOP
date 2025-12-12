import sys
import os
import platform

def onStart():
    print("------------------------------------------------")
    print("DEBUG: Starting Script (Fixed Path)...")

    # --- UPDATED PATH ---
    # We use forward slashes (/) for Python compatibility
    base_path = 'C:/Users/user/.conda/envs/env_Name'
    # --------------------

    print(f"DEBUG: Target Base Path: {base_path}")

    if platform.system().lower() == 'windows':
        
        # Construct sub-paths
        dll_path = base_path + '/DLLs'
        bin_path = base_path + '/Library/bin'
        site_packages = base_path + '/Lib/site-packages'

        # 1. Check Base Folder
        if not os.path.exists(base_path):
            print(f"CRITICAL ERROR: Folder not found! -> {base_path}")
            print("Double check if the folder is '.conda' or just 'conda'.")
            return
        else:
            print("SUCCESS: Base environment folder found.")

        # 2. Check and Add DLLs (Required for Python 3.8+)
        if sys.version_info.major >= 3 and sys.version_info.minor >= 8:
            if os.path.isdir(dll_path):
                os.add_dll_directory(dll_path)
                print("SUCCESS: DLL path added.")
            else:
                print(f"WARNING: DLL folder missing (common in some envs) -> {dll_path}")
                
            if os.path.isdir(bin_path):
                os.add_dll_directory(bin_path)
                print("SUCCESS: Bin path added.")
            else:
                print(f"WARNING: Bin folder missing -> {bin_path}")
        else:
            # Legacy method
            print("INFO: Using legacy PATH method.")
            os.environ['PATH'] = dll_path + os.pathsep + os.environ['PATH']
            os.environ['PATH'] = bin_path + os.pathsep + os.environ['PATH']

        # 3. Add Site-Packages (Libraries)
        if os.path.exists(site_packages):
            if site_packages not in sys.path:
                sys.path.insert(0, site_packages) # Insert at the very top
                print(f"SUCCESS: Site-Packages loaded -> {site_packages}")
            else:
                print("INFO: Site-Packages already loaded.")
        else:
            print(f"CRITICAL ERROR: Site-Packages folder not found! -> {site_packages}")

    print("DEBUG: Script Completed.")
    print("------------------------------------------------")
    return
