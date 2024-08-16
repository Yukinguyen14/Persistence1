import subprocess

def CreateTask():
    task_name = input ("NHập taskname:")
    command_check = f'schtasks /query /tn "{task_name}"'

    try:
        subprocess.run(command_check, shell=True, check=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Task '{task_name}' đã tồn tại")
    except subprocess.CalledProcessError:
        program = r"C:\Windows\System32\notepad.exe"
        schedule = "/SC DAILY /ST 10:42 /RI 10"
        command = f'schtasks /create /tn "{task_name}" /tr "{program}" {schedule}'
    
        try:
            subprocess.run(command, shell=True, check=True)
            print(f"Task '{task_name}' đã được tạo thành công!")
        except subprocess.CalledProcessError as e:
            print(f"Lỗi khi tạo task: {e}")
def ModifyTassk():
    task_name = input ("NHập taskname:")
    check_task = f'schtasks /query /tn {task_name}'
    try:
        subprocess.run(check_task,shell=True,check=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        new_program = r"C:\Windows\System32\notepad.exe"
        schedule = "/SC DAILY /ST 08:00"
        command = f'schtasks /create /tn "{task_name}" /tr "{new_program}" {schedule} /F'
        try:
            subprocess.run(command, shell=True, check=True)
            print(f"Task '{task_name}' đã sửa  thành công!")
        except subprocess.CalledProcessError as e:
            print(f"Lỗi khi sửa task: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Task '{task_name}' không tồn tại")
    
def DeleteTask():
    task_name = input ("NHập taskname:")
    check_task = f'schtasks /query /tn {task_name}'
    try:
        subprocess.run(check_task,shell=True,check=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        command = f'schtasks /delete /tn "{task_name}" /F '
        try:
            subprocess.run(command, shell=True, check=True)
            print(f"Task '{task_name}' đã xóa  thành công!")
        except subprocess.CalledProcessError as e:
            print(f"Lỗi khi sửa task: {e}")
    except subprocess.CalledProcessError:
        print(f"Task '{task_name}' không tồn tại")
def main():
    action = input ("Chọn Tạo(1) Sửa(2) Xóa(3):")
    if action == '1':
        CreateTask()
    elif action == '2':
        ModifyTassk()
    elif action == '3':
        DeleteTask()
    else:
        print("Lựa chọn không phù hợp!")
if __name__ == "__main__":
    main()
