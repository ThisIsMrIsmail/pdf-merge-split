
$sendToDir = "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\SendTo"

if (-not (Test-Path $sendToDir)) {
    New-Item -ItemType Directory -Path $sendToDir
}

$WshShell = New-Object -comObject WScript.Shell

$MergeShortcut = $WshShell.CreateShortcut("$sendToDir\Merge with PDFIY.lnk")
$SplitShortcut = $WshShell.CreateShortcut("$sendToDir\Split with PDFIY.lnk")

# $MergeShortcut.TargetPath = "C:\Users\ismail\dev\side-projects\pdfiy\release\pdify-merge.exe"
# $SplitShortcut.TargetPath = "C:\Users\ismail\dev\side-projects\pdfiy\release\pdify-split.exe"
$MergeShortcut.TargetPath = ".\pdify-merge.exe"
$SplitShortcut.TargetPath = ".\pdify-split.exe"

$MergeShortcut.Save()
$SplitShortcut.Save()