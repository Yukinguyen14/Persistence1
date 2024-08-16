# ‪C:\Windows\System32\cmd.exe
# C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
# C:\Windows\System32\notepad.exe
function ModifyTaskSchedule {
param(
    [string]$Task_name,
    [string]$Execution,
    [string]$Argument = "",
    [datetime]$startTime
    )
    $task = Get-ScheduledTask -TaskName $Task_name
    if($Argument -eq ""){
    $action = New-ScheduledTaskAction -Execute "$Execution"
    }
    else{
    $action = New-ScheduledTaskAction -Execute "$Execution" -Argument "$Argument"
    }
  
    $trigged = New-ScheduledTaskTrigger -Daily -At "$startTime"
    Set-ScheduledTask -TaskName $Task_name -Action $action -Trigger $trigged
    

    if(Get-ScheduledTask -TaskName $Task_name){
        Write-Host " Task '$Task_name' sua thanh cong"}
     else{
        Write-Host "Task '$Task_name' sua khong thanh cong"}  
}

[string]$Taskname = Read-Host -Prompt "Nhap taskname"
$ExecutionPath = Read-Host -Prompt "Nhap path"
$Argument = Read-Host -Prompt "nhap Argument"
$DateInput = Read-Host -Prompt "Nhap thoi gian khoi chay(e.g, 08:00PM)"
$startTime = [datetime]::Parse($DateInput)

if(Get-ScheduledTask -TaskName $Taskname -ErrorAction SilentlyContinue){
    ModifyTaskSchedule -Task_name $Taskname -Execution $ExecutionPath -Argument $Argument -startTime $startTime
}
else{
    Write-Host "Task '$Taskname' khong ton tai"
}

