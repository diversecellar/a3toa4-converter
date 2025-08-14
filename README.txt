README

PURPOSE
This little app, built i the PowerShell 7.5+ and Python 3.9+ languages (w/ versions), was built to aid my department at my university (redacted) in scanning exam scripts and processing them for storage and provision of external moderation. Usually, one would scan each page of a double-paged booklet (i.e. page on left then page on right) sequentially and individually. This can easily take 3 hours for just 20 scripts. Then, each file then has to be processed individually.

Now, with this app, you can scan the booklet as-is, in A3 form (page by page), saving 60% of scanning time and then, at the click of a button it converts all the A3s into A4s. Thus saving time lost to painful admin tasks.

BUILD
1) open powershell terminal in the home directory of this app
2) run "powershell.exe .\ps-base\macro.ps1" in the shell

INSTALLATION:
1a) If windows python
already exists, the app will use it automatically
1b) If not, you must click the installer and when it prompts for admin privileges, say "Yes"
2) Installation is quick and takes about 3-5 minutes

USAGE:
1) Once installation is done you go back to the program director and will see "converter-app.exe"
2) You click the converter-app.exe, it prompts you for the directory where you have your scans and outputs. Say you have saved your a3 scans to a folder on the Desktop named "CIV2011F Scans", then you must click that folder. 

Then the program will run which runs at a rate of about 0.25 seconds per scan. Once scanned, it save the outputs in the same folder but in a subfolder Called "CIV2011F Scans - A4 Outputs"
