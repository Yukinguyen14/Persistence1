
import subprocess

def CreateKey():
   key_path = input("Nhập key path:")
   value_name = input("Nhập keyname:")
   value_data = input("Nhập data:")
   
   command_check = f'reg query "{key_path}" /v "{value_name}" '
   try:
       subprocess.run(command_check,shell=True,check=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
       print(f"Reg '{value_name}' đã tồn tại trong '{key_path}' ") 
   except subprocess.CalledProcessError:
        command_create = f'reg add {key_path} /v {value_name} /t REG_SZ /d {value_data} /f'
        try:
            subprocess.run(command_create,shell=True,check=True)
            print(f"Reg '{value_name}' được tạo thành công trong '{key_path}'")
        except subprocess.CalledProcessError as e: 
            print(f"Lỗi khi tạo Reg '{e}'")
        
def ModifyReg():
    key_path = input("Nhập key path:")
    value_name = input("Nhập keyname:")
    new_value_data = input("Nhập data:")
    
    command_check = f'reg query "{key_path}" /v "{value_name}" '
    try:
        subprocess.run(command_check,shell=True,check=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        command_modify = f'reg add {key_path} /v {value_name} /t REG_SZ /d {new_value_data} /f'
        try:
            subprocess.run(command_modify,shell=True,check=True)
            print(f"Reg '{value_name}' được sửa thành công trong '{key_path}'")
        except subprocess.CalledProcessError as e: 
            print(f"Lỗi khi sửa Reg '{e}'")
    except subprocess.CalledProcessError:
        print(f"Reg '{value_name}' không tồn tại trong '{key_path}' ") 
        
def DeleteReg():
    key_path = input("Nhập key path:")
    value_name = input("Nhập keyname:")
    
    command_check = f'reg query "{key_path}" /v "{value_name}"  '
    try:
        subprocess.run(command_check,shell=True,check=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        command_detele = f'reg delete {key_path}  /f'
        try:
            subprocess.run(command_detele,shell=True,check=True)
            print(f"Reg '{value_name}' được xóa thành công trong '{key_path}'")
        except subprocess.CalledProcessError as e: 
            print(f"Lỗi khi xóa Reg '{e}'")
    except subprocess.CalledProcessError:
        print(f"Reg '{value_name}' không tồn tại!")
        
def main():
    action = input ("Chọn Tạo(1) Sửa(2) Xóa(3):")
    if action == '1':
        CreateKey()
    elif action == '2':
        ModifyReg()
    elif action == '3':
        DeleteReg()
    else:
        print("Lựa chọn không phù hợp!")
if __name__ == "__main__":
    main()


# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
# C:\Windows\System32\notepad.exe