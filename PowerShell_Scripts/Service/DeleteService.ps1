
# C:\Windows\system32\svchost.exe
# # ‪C:\Windows\System32\cmd.exe
# C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
# C:\Windows\System32\notepad.exe

[string]$servicename = Read-Host -Prompt "Nhap service"
$service = Get-Service -Name $servicename -ErrorAction SilentlyContinue
if($service){
    if($service.Status -ne 'Stopped'){
    Stop-Service -Name $servicename -Force
    }
    sc.exe delete $servicename
    Write-Host " Xoa service thanh cong"
}else{
    Write-Host "Service ko ton tai!"
    }