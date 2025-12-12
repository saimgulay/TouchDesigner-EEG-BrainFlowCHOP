import sys
import os
import platform

def onStart():
    print("------------------------------------------------")
    print("DEBUG: Starting Script...")

    # --- CONFIGURATION ---
    user = 'janni'           
    condaEnv = 'TD'          
    conda_folder = 'miniconda3' # Change to 'anaconda3' if needed
    # ---------------------

    print(f"DEBUG: Target User: {user}")
    print(f"DEBUG: Target Environment: {condaEnv}")
    print(f"DEBUG: Current TD Python Version: {sys.version}")

    if platform.system().lower() == 'windows':
        # Construct paths
        base_path = f'C:/Users/{user}/{conda_folder}/envs/{condaEnv}'
        dll_path = base_path + '/DLLs'
        bin_path = base_path + '/Library/bin'
        site_packages = base_path + '/Lib/site-packages'

        print(f"DEBUG: Checking base path: {base_path}")

        # 1. Check Base Folder
        if not os.path.exists(base_path):
            print(f"CRITICAL ERROR: Base environment folder not found! -> {base_path}")
            print("Please check your 'user' or 'conda_folder' variables.")
            return
        else:
            print("SUCCESS: Base environment folder exists.")

        # 2. Check and Add DLLs
        if os.path.exists(dll_path):
            try:
                os.add_dll_directory(dll_path)
                print(f"SUCCESS: DLL path added -> {dll_path}")
            except Exception as e:
                print(f"ERROR: Issue adding DLL path: {e}")
        else:
            print(f"WARNING: DLL folder not found! -> {dll_path}")

        # 3. Check and Add Bin
        if os.path.exists(bin_path):
            try:
                os.add_dll_directory(bin_path)
                print(f"SUCCESS: Bin path added -> {bin_path}")
            except Exception as e:
                print(f"ERROR: Issue adding Bin path: {e}")
        else:
            print(f"WARNING: Bin folder not found! -> {bin_path}")

        # 4. Check and Add Site-Packages (Libraries)
        if os.path.exists(site_packages):
            if site_packages not in sys.path:
                sys.path.insert(0, site_packages) # Insert at the very top of the list
                print(f"SUCCESS: Site-Packages added to sys.path[0].")
                print(f"DEBUG: Path -> {site_packages}")
            else:
                print("INFO: Site-Packages is already in sys.path.")
        else:
            print(f"CRITICAL ERROR: Site-Packages folder missing! -> {site_packages}")
            print("If this folder is missing, you cannot import external libraries.")

    else:
        print("DEBUG: System is not Windows. Skipping Windows-specific setup...")

    print("DEBUG: Script Completed.")
    print("------------------------------------------------")
    return
