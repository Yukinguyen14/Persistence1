# HKCU:\Software\Microsoft\Windows\CurrentVersion\Run



$registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
$name = Read-Host -Prompt "Nhap name"
$value = Read-Host -Prompt "Nhap gia tri"

New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType String -Force

Write-Host "Da them gia tri vao registry."
