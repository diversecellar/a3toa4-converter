# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 12:56:50 2025

@author: Paul Namalomba
"""

# =====================================================================================
# IMPORTS AND DEPENDENCIES
# =====================================================================================
import subprocess
import os
import sys
import glob
from pathlib import Path


# =====================================================================================
# WORKING DIRECTORY SETUP AND CONFIGURATION
# =====================================================================================
fixed_code_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(fixed_code_path)
os.chdir('..')
cwd_dir = os.getcwd()


# =====================================================================================
# PYTHON INSTALLATION DETECTION AND PATH RESOLUTION
# =====================================================================================
# Path to a Python interpreter that runs any Python script
# under the virtualenv /path/to/virtualenv/
def find_python_installation():
    """
    Checks if Python is installed and attempts to find its executable path.
    """
    try:
        # sys.executable returns the absolute path of the Python interpreter executable
        python_executable_path = sys.executable
        #print(f"Python is installed. Executable path: {python_executable_path}")

        # Optionally, check the directory where the executable resides
        python_install_dir = os.path.dirname(python_executable_path)
        #print(f"Python installation directory: {python_install_dir}")

        # Check for python.exe in the same directory (common for standard installations)
        python_exe_in_dir = os.path.join(python_install_dir, "python.exe")
        if os.path.exists(python_exe_in_dir):
            #print(f"python.exe found at: {python_exe_in_dir}")
            return Path(python_exe_in_dir)
        else:
            print("python.exe not found directly in the executable's directory.")
            return Path(os.path.join(cwd_dir, "py3", "Scripts", "python.exe"))

    except Exception as e:
        print(f"An error occurred while trying to find Python: {e}")
        print("Python might not be correctly installed or configured in the system PATH.")


# =====================================================================================
# MAIN EXECUTION BLOCK - PYTHON DISCOVERY AND VALIDATION
# =====================================================================================

try:
    if __name__ == "__main__":
        python_bin = find_python_installation()
        python_bin = python_bin.as_posix()
        print(f"python.exe found at: {python_bin}")
        #print(python_bin)
    #python_bin = Path(os.path.join(cwd_dir, "py3", "Scripts", "python.exe")).as_posix()

        
# =====================================================================================
# ERROR HANDLING - PYTHON INSTALLATION VALIDATION
# =====================================================================================
except Exception as e:
    print(e)
    print("You have not yet installed python locally or globally")
    sys.exit()


# =====================================================================================
# SCRIPT EXECUTION - LAUNCH CONVERTER APPLICATION
# =====================================================================================
# Path to the script that must run under the virtualenv
#glob.glob()
script_file = Path(os.path.join(cwd_dir, "src", "converter.py")).as_posix()
subprocess.Popen([python_bin, script_file])