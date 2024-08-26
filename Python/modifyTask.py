import win32com.client
def update_task(task_name, new_exe_path=None, new_trigger_time=None):
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()
    rootFolder = scheduler.GetFolder("\\")
    try:
        task = rootFolder.GetTask(task_name)
        taskDef = task.Definition
        
        if new_trigger_time:
            for trigger in taskDef.Triggers:
                trigger.StartBoundary = new_trigger_time  

        if new_script_path:
            for action in taskDef.Actions:
                action.Path = new_exe_path               

        # Đăng ký lại task với các thay đổi
        rootFolder.RegisterTaskDefinition(
            task_name,
            taskDef,
            6,  # TASK_CREATE_OR_UPDATE
            None,  # Người dùng hiện tại
            None,  # Mật khẩu
            3,  # TASK_LOGON_INTERACTIVE_TOKEN
        )

        print(f"Task '{task_name}' đã được cập nhật thành công.")
    except Exception as e:
        print(f"Không thể sửa task '{task_name}': {e}")
if __name__ == "__main__":
    task_name = "RunNotePad"  
    new_script_path = r"C:\Users\Admin\Downloads\Garena-v2.0-VN.exe"  
    new_trigger_time = "2024-08-26T08:52:00" 

    update_task(task_name, new_script_path, new_trigger_time)
