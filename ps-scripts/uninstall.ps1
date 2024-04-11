Remove-Item "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\SendTo\Merge with PDFIY.lnk" -Force
Remove-Item "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\SendTo\Split with PDFIY.lnk" -Force

Get-ChildItem -Path C:\pdfiy -Include *.* -File -Recurse | foreach { $_.Delete()}
Remove-Item $PSCommandPath -Force
Remove-Item -Recurse -Force C:\pdfiy