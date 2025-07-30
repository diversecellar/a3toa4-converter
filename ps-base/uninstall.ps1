# uninstall.ps1
# Deletes everything in its own directory (including itself), then cd’s up one level.
cd ..

# Get the full path to this script
$scriptPath = $MyInvocation.MyCommand.Definition
$scriptDir  = Split-Path $scriptPath
$scriptName = Split-Path $scriptPath -Leaf

# Determine the parent directory
$parentDir = Split-Path $scriptDir

# 1. Remove all files/folders in this directory except the running script
Get-ChildItem -Path $scriptDir -Force |
  Where-Object { $_.FullName -ne $scriptPath } |
  Remove-Item -Recurse -Force

# 2. Change into the parent directory
Set-Location $parentDir

# 3. Remove this script file itself
Remove-Item -LiteralPath $scriptPath -Force