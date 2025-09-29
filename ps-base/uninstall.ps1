# ===================================================================================
# A3 TO A4 CONVERTER UNINSTALLER
# ===================================================================================
# uninstall.ps1
# Deletes everything in its own directory (including itself), then cd's up one level.

# ===================================================================================
# INITIAL DIRECTORY NAVIGATION
# ===================================================================================
cd ..

# ===================================================================================
# SCRIPT PATH DETECTION AND ANALYSIS
# ===================================================================================
# Get the full path to this script
$scriptPath = $MyInvocation.MyCommand.Definition
$scriptDir  = Split-Path $scriptPath
$scriptName = Split-Path $scriptPath -Leaf

# -------------------------------------------------------------------------
# PARENT DIRECTORY DETERMINATION
# -------------------------------------------------------------------------
# Determine the parent directory
$parentDir = Split-Path $scriptDir.ps1
# Deletes everything in its own directory (including itself), then cd’s up one level.
cd ..

# Get the full path to this script
$scriptPath = $MyInvocation.MyCommand.Definition
$scriptDir  = Split-Path $scriptPath
$scriptName = Split-Path $scriptPath -Leaf

# -------------------------------------------------------------------------
# PARENT DIRECTORY DETERMINATION
# -------------------------------------------------------------------------
# Determine the parent directory
$parentDir = Split-Path $scriptDir


# ===================================================================================
# APPLICATION REMOVAL PROCESS
# ===================================================================================

# -------------------------------------------------------------------------
# SELECTIVE FILE AND FOLDER REMOVAL
# -------------------------------------------------------------------------
# 1. Remove all files/folders in this directory except the running script
Get-ChildItem -Path $scriptDir -Force |
  Where-Object { $_.FullName -ne $scriptPath } |
  Remove-Item -Recurse -Force

# -------------------------------------------------------------------------
# DIRECTORY NAVIGATION FOR CLEANUP
# -------------------------------------------------------------------------
# 2. Change into the parent directory
Set-Location $parentDir

# -------------------------------------------------------------------------
# SELF-DESTRUCTION - REMOVE UNINSTALLER SCRIPT
# -------------------------------------------------------------------------
# 3. Remove this script file itself
Remove-Item -LiteralPath $scriptPath -Force