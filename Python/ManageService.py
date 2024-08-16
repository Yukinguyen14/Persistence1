import subprocess

def CreateService():
    service_name = input("Nhập tên service:")
    path = input("Nhap path:")
    command_check = f'sc query "{service_name}"'
    result = subprocess.run(command_check, shell=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if(result.returncode == 0 ):
        print(f"Service '{service_name}' đã tồn tại")
    else:
        comman_create = f'sc create {service_name} binPath="{path}" '
        subprocess.run(comman_create,shell=True,check=True)
        print(f"Tạo service thành công")

def ModifyService():
    service_name = input("Nhập tên service:")
    new_path = input("Nhap path:")
    command_check = f'sc query "{service_name}"'
    result = subprocess.run(command_check, shell=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if(result.returncode == 0):
        comman_modify = f'sc config {service_name} binPath= {new_path}'
        subprocess.run(comman_modify,shell=True,check=True)
        print(f"Sửa service  '{service_name}' thành công")
    else:
        print(f"Service  '{service_name}' không tồn tại")
def DeleteService():
    service_name = input("Nhập tên service:")
    command_check = f'sc query "{service_name}"'
    result = subprocess.run(command_check, shell=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if(result.returncode == 0):
        command_delete = f'sc delete {service_name}'
        subprocess.run(command_delete,shell=True,check=True)
        print(f"Xóa service  '{service_name}' thành công")
    else:
        print(f"Service  '{service_name}' không tồn tại")
def main():
    action = input ("Chọn Tạo(1) Sửa(2) Xóa(3):")
    if action == '1':
        CreateService()
    elif action == '2':
        ModifyService()
    elif action == '3':
        DeleteService()
    else:
        print("Lựa chọn không phù hợp!")
if __name__ == "__main__":
    main()