import win32com.client

def delete_task(task_name):
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()

    rootFolder = scheduler.GetFolder("\\")

    try:
        # Xóa task
        rootFolder.DeleteTask(task_name, 0)  
        print(f"Task '{task_name}' đã được xóa thành công.")

    except Exception as e:
        print(f"Không thể xóa task '{task_name}': {e}")

if __name__ == "__main__":
    task_name = "RunNotePad" 

    delete_task(task_name)
