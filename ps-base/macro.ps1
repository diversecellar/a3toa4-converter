# ===================================================================================
# A3 TO A4 CONVERTER - BUILD AUTOMATION SCRIPT
# ===================================================================================
# compile build\*.ps1 files into .\*.exe

# ===================================================================================
# SCRIPT PATH RESOLUTION AND WORKING DIRECTORY SETUP
# ===================================================================================
# Full path to the currently running script
$scriptFullPath = $MyInvocation.MyCommand.Definition

# Directory portion only
$scriptDirectory = Split-Path $scriptFullPath -Parent
cd $scriptDirectory
cd ..


# ===================================================================================
# DIRECTORY STRUCTURE CREATION AND VALIDATION
# ===================================================================================
# Create ps-base directory if it doesn't exist
$basepath = Join-Path -Path $PWD.Path -ChildPath "ps-base"
if (-not (Test-Path -Path $basepath -PathType Container)) {
    New-Item -Path $basepath -ItemType Directory
}

# Create uninstall directory if it doesn't exist
$uninstallpath = Join-Path -Path $PWD.Path -ChildPath "uninstall"
if (-not (Test-Path -Path $uninstallpath -PathType Container)) {
    New-Item -Path $uninstallpath -ItemType Directory
}


# ===================================================================================
# UNINSTALLER EXECUTABLE COMPILATION
# ===================================================================================
# Build uninstaller executable from PowerShell script
$uninstallpspath = Join-Path -Path $basepath -ChildPath "uninstall.ps1"
$uninstallexepath = Join-Path -Path $uninstallpath -ChildPath "uninstall.exe"
ps2exe $uninstallpspath $uninstallexepath -Title "UN-Installer for A3 to A4 PDF converter" -Company "diversecellar" -Copyright "Copyright (c) 2025 diversecellar"


# ===================================================================================
# INSTALLER EXECUTABLE COMPILATION
# ===================================================================================
# Build installer executable from PowerShell script
$installpspath = Join-Path -Path $basepath -ChildPath "installer.ps1"
$installexepath = Join-Path -Path $PWD.Path -ChildPath "installer.exe"
ps2exe $installpspath $installexepath -Title "Installer for A3 to A4 PDF converter" -Company "diversecellar" -Copyright "Copyright (c) 2025 diversecellar"

