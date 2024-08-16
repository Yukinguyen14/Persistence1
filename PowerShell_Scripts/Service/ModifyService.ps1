
# C:\Windows\system32\svchost.exe
# # ‪C:\Windows\System32\cmd.exe
# C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
# C:\Windows\System32\notepad.exe

[string]$servicename = Read-Host -Prompt "Nhap service"
$service = Get-Service -Name $servicename -ErrorAction SilentlyContinue
if($service){
    Set-Service -Description "This is test service" -StartupType Manual
    Write-Host " Sua service thanh cong"
}else{
    Write-Host "Service ko ton tai!"
    }

