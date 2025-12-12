import sys
import os
import platform

def onStart():
    # --- CONFIGURATION START ---
    
    # 1. Your Windows Username (Check C:/Users/)
    # Was 'saimgulay' in your first screenshot, 'janni' in your second.
    user = 'username' 

    # 2. Your Environment Name (Check 'conda env list')
    condaEnv = 'env_Name' 

    # 3. Your Conda Installation Type
    # Change this to 'anaconda3' if you installed the full Anaconda version.
    conda_folder = 'miniconda3' 

    # --- CONFIGURATION END ---

    if platform.system().lower() == 'windows':
        # Construct the base path to your environment
        env_path = f'C:/Users/{user}/{conda_folder}/envs/{condaEnv}'
        
        dll_path = env_path + '/DLLs'
        bin_path = env_path + '/Library/bin'
        site_packages = env_path + '/Lib/site-packages'

        # Check if the path actually exists before trying to load it
        if not os.path.exists(env_path):
            print(f"ERROR: Could not find Conda Env at: {env_path}")
            print("Check your 'user', 'condaEnv', and 'conda_folder' variables.")
            return

        # Add DLLs (Required for Python 3.8+)
        if sys.version_info.major >= 3 and sys.version_info.minor >= 8:
            if os.path.isdir(dll_path):
                os.add_dll_directory(dll_path)
            if os.path.isdir(bin_path):
                os.add_dll_directory(bin_path)
        else:
            # Legacy method
            os.environ['PATH'] = dll_path + os.pathsep + os.environ['PATH']
            os.environ['PATH'] = bin_path + os.pathsep + os.environ['PATH']

        # Add site-packages so Python can find your installed libraries
        if site_packages not in sys.path:
            sys.path = [site_packages] + sys.path
            
        print(f"SUCCESS: Loaded Conda Environment: {condaEnv}")
    
    else:
        # MacOS Setup
        base_mac = f'/opt/{conda_folder}/envs/{condaEnv}'
        os.environ['PATH'] = base_mac + '/lib' + os.pathsep + os.environ['PATH']
        os.environ['PATH'] = base_mac + '/bin' + os.pathsep + os.environ['PATH']
        
        # Note: Check your specific python version number here (e.g. python3.11)
        sys.path = [base_mac + '/lib/python3.11/site-packages'] + sys.path

    return
