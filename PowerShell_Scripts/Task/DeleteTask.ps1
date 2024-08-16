# ‪C:\Windows\System32\cmd.exe
# C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
# C:\Windows\System32\notepad.exe
function DeleteTaskSchedule {
param(
    [string]$Task_name
    )
    
    Unregister-ScheduledTask -TaskName $Task_name -Confirm:$false -ErrorAction SilentlyContinue

    if(Get-ScheduledTask -TaskName $Task_name -ErrorAction SilentlyContinue){
        Write-Host " Task '$Task_name' xoa khong thanh cong"}
     else{
        Write-Host "Task '$Task_name' xoa thanh cong"}  
}

[string]$Taskname = Read-Host -Prompt "Nhap taskname"

if(Get-ScheduledTask -TaskName $Taskname -ErrorAction SilentlyContinue){
    DeleteTaskSchedule -Task_name $Taskname
}
else{
    Write-Host "Task '$Taskname' khong tim thay!"
}