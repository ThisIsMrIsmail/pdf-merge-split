
$sendToDir = "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\SendTo"

if (-not (Test-Path $sendToDir)) {
    New-Item -ItemType Directory -Path $sendToDir
}

$WshShell = New-Object -comObject WScript.Shell

$PdifyMergeShortcut = $WshShell.CreateShortcut("$sendToDir\Merge with PDFIY.lnk")
$PdifySplitShortcut = $WshShell.CreateShortcut("$sendToDir\Split with PDFIY.lnk")

$PdifyMergeShortcut.TargetPath = "C:\Users\ismail\dev\side-projects\pdfiy\dist\merge.exe"
$PdifySplitShortcut.TargetPath = "C:\Users\ismail\dev\side-projects\pdfiy\dist\split.exe"

$PdifyMergeShortcut.Save()
$PdifySplitShortcut.Save()