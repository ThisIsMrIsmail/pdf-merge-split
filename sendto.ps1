
$sendToDir = "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\SendTo"

if (-not (Test-Path $sendToDir)) {
    New-Item -ItemType Directory -Path $sendToDir
}

Copy-Item -Path "./dist/merge.exe" -Destination $sendToDir
Copy-Item -Path "./dist/split.exe" -Destination $sendToDir