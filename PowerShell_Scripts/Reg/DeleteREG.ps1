# HKCU:\Software\Microsoft\Windows\CurrentVersion\Run



$registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
$name = Read-Host -Prompt "Nhap name"


Remove-ItemProperty -Path $registryPath -Name $name -Force

Write-Host "Da xoa registry."
