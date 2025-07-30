# compile build\*.ps1 files into .\*.exe
# Full path to the currently running script
$scriptFullPath = $MyInvocation.MyCommand.Definition

# Directory portion only
$scriptDirectory = Split-Path $scriptFullPath -Parent
cd $scriptDirectory
cd ..

$basepath = Join-Path -Path $PWD.Path -ChildPath "ps-base"
if (-not (Test-Path -Path $basepath -PathType Container)) {
    New-Item -Path $basepath -ItemType Directory
}
$uninstallpath = Join-Path -Path $PWD.Path -ChildPath "uninstall"
if (-not (Test-Path -Path $uninstallpath -PathType Container)) {
    New-Item -Path $uninstallpath -ItemType Directory
}
$uninstallpspath = Join-Path -Path $basepath -ChildPath "uninstall.ps1"
$uninstallexepath = Join-Path -Path $uninstallpath -ChildPath "uninstall.exe"
ps2exe $uninstallpspath $uninstallexepath -Title "UN-Installer for A3 to A4 PDF converter" -Company "diversecellar" -Copyright "Copyright (c) 2025 diversecellar"
$installpspath = Join-Path -Path $basepath -ChildPath "installer.ps1"
$installexepath = Join-Path -Path $PWD.Path -ChildPath "installer.exe"
ps2exe $installpspath $installexepath -Title "Installer for A3 to A4 PDF converter" -Company "diversecellar" -Copyright "Copyright (c) 2025 diversecellar"

