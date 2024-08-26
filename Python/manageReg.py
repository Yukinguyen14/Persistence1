
import winreg 

def CreateKey():
    key_path = input("Nhập key path:")
    value_name = input("Nhập keyname:")
    value_data = input("Nhập data:")
   
    # Kiểm tra xem key đã tồn tại chưa
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ) as key:
        # Kiểm tra xem giá trị đã tồn tại chưa
        try:
            winreg.QueryValueEx(key, value_name)
            print(f"Registry key '{key_path}' và giá trị '{value_name}' đã tồn tại.")
        except FileNotFoundError:
            print(f"Key không tồn tại")
            try:
                with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
                    winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)
                    print(f"Registry key '{key_path}' đã được tạo và giá trị '{value_data}' đã được thiết lập.")
            except WindowsError as e:
                print(f"Đã xảy ra lỗi khi tạo key hoặc thiết lập giá trị: {e}")

        
def ModifyReg():
    key_path = input("Nhập key path:")
    value_name = input("Nhập keyname:")
    new_value_data = input("Nhập data:")
    
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ) as key:
        try:
            winreg.QueryValueEx(key,value_name)
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path,0,winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key,value_name,0,winreg.REG_SZ,new_value_data)
                print(f"Sửa REG thành công!")
            
        except FileNotFoundError:
            print(f" '{value_name}' không tồn tại!")
        
def DeleteReg():
    key_path = input("Nhập key path:")
    value_name = input("Nhập keyname:")
    
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER,key_path,0,winreg.KEY_READ) as key:
        try:
            winreg.QueryValueEx(key,value_name)
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER,key_path,0,winreg.KEY_WRITE) as key:
                winreg.DeleteValue(key,value_name)
                print(f"Xóa REG '{value_name}' thành công!")
        except FileNotFoundError:
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


#key_path = Software\Microsoft\Windows\CurrentVersion\Run
#key_name = AutoNotepad
#value_data = C:\Windows\System32\notepad.exe
#new_value_data = C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
