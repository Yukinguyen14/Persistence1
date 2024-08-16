# HKCU:\Software\Microsoft\Windows\CurrentVersion\Run



$registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
$name = Read-Host -Prompt "Nhap name"
$value = Read-Host -Prompt "Nhap gia tri"


Set-ItemProperty -Path $registryPath -Name $name -Value $value  -Force

Write-Host "Da sua gia tri vao registry."
