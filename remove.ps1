Get-ChildItem -Path C:\pdfiy -Include *.* -File -Recurse | foreach { $_.Delete()}
Remove-Item -Recurse -Force C:\pdfiy
Remove-Item $PSCommandPath -Force