
$pdfiy_folder = "C:\pdfiy"
$send_to_dir = "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\SendTo"

if (-not (Test-Path $pdfiy_folder)) {
    New-Item -ItemType Directory -Path $pdfiy_folder
}
if (-not (Test-Path $send_to_dir)) {
    New-Item -ItemType Directory -Path $sendToDir
}

Copy-Item -Path *.* -Destination $pdfiy_folder

$WshShell = New-Object -comObject WScript.Shell

$MergeShortcut = $WshShell.CreateShortcut("$send_to_dir\Merge with PDFIY.lnk")
$SplitShortcut = $WshShell.CreateShortcut("$send_to_dir\Split with PDFIY.lnk")

$MergeShortcut.TargetPath = "$pdfiy_folder\pdfiy-merge.exe"
$SplitShortcut.TargetPath = "$pdfiy_folder\pdfiy-split.exe"

$MergeShortcut.Save()
$SplitShortcut.Save()