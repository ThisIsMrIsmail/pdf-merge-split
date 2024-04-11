
$sendToDir = "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\SendTo"

if (-not (Test-Path $sendToDir)) {
    New-Item -ItemType Directory -Path $sendToDir
}

$WshShell = New-Object -comObject WScript.Shell

$MergeShortcut = $WshShell.CreateShortcut("$sendToDir\Merge with PDFIY.lnk")
$SplitShortcut = $WshShell.CreateShortcut("$sendToDir\Split with PDFIY.lnk")

$curr_dir = Get-Location

$MergeShortcut.TargetPath = "$curr_dir\pdfiy-merge.exe"
$SplitShortcut.TargetPath = "$curr_dir\pdfiy-split.exe"

$MergeShortcut.Save()
$SplitShortcut.Save()