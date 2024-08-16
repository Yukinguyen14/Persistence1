# C:\Windows\system32\svchost.exe
# # ‪C:\Windows\System32\cmd.exe
# C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
# C:\Windows\System32\notepad.exe


$ServiceName = Read-Host -Prompt "Nhap ten"
if(Get-Service -Name $ServiceName -ErrorAction SilentlyContinue){
    Write-Host " Service Name da ton tai!"
    }
else{

$Path = Read-Host -Prompt "Nhap path"
$DisplayName = Read-Host -Prompt "Nhap Displayname"
$Description = Read-Host -Prompt "Nhap descript"
$StartType = Read-Host -Prompt "Nhap type"

New-Service -Name $ServiceName -BinaryPathName $Path -DisplayName $DisplayName -Description $Description -StartupType $StartType
Write-Host " Tao service thanh cong"
}


