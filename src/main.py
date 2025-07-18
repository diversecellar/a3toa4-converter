# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 12:56:50 2025

@author: Paul Namalomba
"""

import subprocess
import os
from pathlib import Path

fixed_code_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(fixed_code_path)
os.chdir('..')
cwd_dir = os.getcwd()

# Path to a Python interpreter that runs any Python script
# under the virtualenv /path/to/virtualenv/
python_bin = Path(os.path.join(cwd_dir, "py3", "Scripts", "python.exe")).as_posix()

# Path to the script that must run under the virtualenv
script_file = Path(os.path.join(cwd_dir, "src", "converter.py")).as_posix()

subprocess.Popen([python_bin, script_file])