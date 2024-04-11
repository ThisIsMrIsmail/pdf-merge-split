$send_to_dir = "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\SendTo"

$MergeShortcut = $WshShell.CreateShortcut("$send_to_dir\Merge with PDFIY.lnk")
$SplitShortcut = $WshShell.CreateShortcut("$send_to_dir\Split with PDFIY.lnk")

Get-ChildItem -Path C:\pdfiy -Include *.* -File -Recurse | foreach { $_.Delete()}
Remove-Item $PSCommandPath -Force
Remove-Item -Recurse -Force C:\pdfiy