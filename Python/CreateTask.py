import win32com.client
def create_task(task_name, exe_path, trigger_time="2024-08-26T08:00:00"):
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()
    rootFolder = scheduler.GetFolder("\\")
    # Tạo tác vụ
    taskDef = scheduler.NewTask(0)
    # Cài đặt thời gian trigger
    trigger = taskDef.Triggers.Create(1)  
    trigger.StartBoundary = trigger_time  
    # Cài đặt hành động
    action = taskDef.Actions.Create(0)  
    action.Path = exe_path
    # Các cài đặt khác
    taskDef.RegistrationInfo.Description = "Task to run Python script"
    taskDef.Settings.Enabled = True
    taskDef.Settings.StopIfGoingOnBatteries = False
    # Đăng ký tác vụ trong Task Scheduler
    rootFolder.RegisterTaskDefinition(
        task_name,  # Tên task
        taskDef,
        6,  # TASK_CREATE_OR_UPDATE
        None,  # Người dùng hiện tại
        None,  # Mật khẩu
        3,  # TASK_LOGON_INTERACTIVE_TOKEN
    )
if __name__ == "__main__":
    task_name = "RunNotePad"
    exe_path = r"C:\Windows\notepad.exe"
    trigger_time = "2024-08-26T08:52:00"  

    create_task(task_name, exe_path, trigger_time)
