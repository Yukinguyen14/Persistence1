import ctypes
from ctypes import wintypes

# Các hằng số
SC_MANAGER_CREATE_SERVICE = 0x0002
SC_MANAGER_QUERY_STATUS = 0x0004
SERVICE_WIN32_OWN_PROCESS = 0x00000010
SERVICE_DEMAND_START = 0x00000003
SERVICE_ERROR_NORMAL = 0x00000001

# Tải các thư viện DLL cần thiết
advapi32 = ctypes.WinDLL('advapi32')
kernel32 = ctypes.WinDLL('kernel32')

# Định nghĩa các prototype của hàm
OpenSCManager = advapi32.OpenSCManagerA
CreateService = advapi32.CreateServiceA
ChangeServiceConfig = advapi32.ChangeServiceConfigA
DeleteService = advapi32.DeleteService
CloseServiceHandle = advapi32.CloseServiceHandle
OpenService = advapi32.OpenServiceA

# Định nghĩa loại tham số và kiểu trả về của các hàm
OpenSCManager.argtypes = [wintypes.LPCSTR, wintypes.LPCSTR, wintypes.DWORD]
CreateService.argtypes = [
    wintypes.HANDLE, wintypes.LPCSTR, wintypes.LPCSTR, wintypes.DWORD, wintypes.DWORD,
    wintypes.DWORD, wintypes.DWORD, wintypes.LPCSTR, wintypes.LPCSTR, wintypes.LPDWORD,
    wintypes.LPCSTR, wintypes.LPCSTR, wintypes.LPCSTR
]
CreateService.restype = wintypes.HANDLE
ChangeServiceConfig.argtypes = [
    wintypes.HANDLE, wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, wintypes.LPCSTR,
    wintypes.LPCSTR, wintypes.LPDWORD, wintypes.LPCSTR, wintypes.LPCSTR, wintypes.LPCSTR,
    wintypes.LPCSTR
]
ChangeServiceConfig.restype = wintypes.BOOL
DeleteService.argtypes = [wintypes.HANDLE]
CloseServiceHandle.argtypes = [wintypes.HANDLE]
OpenService.argtypes = [wintypes.HANDLE, wintypes.LPCSTR, wintypes.DWORD]

def create_service(service_name, executable_path, display_name):
    # Mở kết nối đến Service Control Manager với quyền tạo dịch vụ
    scm = OpenSCManager(None, None, SC_MANAGER_CREATE_SERVICE)
    if not scm:
        raise Exception("Mở Service Control Manager thất bại")

    # Tạo dịch vụ mới
    service = CreateService(
        scm,
        service_name.encode('ascii'),
        display_name.encode('ascii'),
        0x000F01FF,  # Quyền truy cập dịch vụ: QUERY_STATUS, START, STOP
        SERVICE_WIN32_OWN_PROCESS,
        SERVICE_DEMAND_START,
        SERVICE_ERROR_NORMAL,
        executable_path.encode('ascii'),
        None,
        None,
        None,
        None,
        None
    )

    if not service:
        CloseServiceHandle(scm)
        raise Exception("Tạo dịch vụ thất bại")

    CloseServiceHandle(service)
    CloseServiceHandle(scm)
    print(f"Dịch vụ '{service_name}' đã được tạo.")

def update_service(service_name, executable_path=None, start_type=None):
    # Mở kết nối đến Service Control Manager với quyền thay đổi cấu hình dịch vụ
    scm = OpenSCManager(None, None, SC_MANAGER_QUERY_STATUS)
    if not scm:
        raise Exception("Mở Service Control Manager thất bại")

    # Mở dịch vụ cần cập nhật
    service = OpenService(scm, service_name.encode('ascii'), 0x0002)  # Quyền thay đổi cấu hình dịch vụ
    if not service:
        CloseServiceHandle(scm)
        raise Exception("Mở dịch vụ thất bại")

    # Cập nhật cấu hình dịch vụ
    result = ChangeServiceConfig(
        service,
        SERVICE_WIN32_OWN_PROCESS,
        start_type if start_type else SERVICE_DEMAND_START,
        SERVICE_ERROR_NORMAL,
        executable_path.encode('ascii') if executable_path else None,
        None,
        None,
        None,
        None,
        None,
        None
    )

    if not result:
        CloseServiceHandle(service)
        CloseServiceHandle(scm)
        raise Exception("Cập nhật cấu hình dịch vụ thất bại")

    CloseServiceHandle(service)
    CloseServiceHandle(scm)
    print(f"Dịch vụ '{service_name}' đã được cập nhật.")

def delete_service(service_name):
    # Mở kết nối đến Service Control Manager với quyền truy vấn trạng thái dịch vụ
    scm = OpenSCManager(None, None, SC_MANAGER_QUERY_STATUS)
    if not scm:
        raise Exception("Mở Service Control Manager thất bại")

    # Mở dịch vụ cần xóa
    service = OpenService(scm, service_name.encode('ascii'), 0x0001)  # Quyền truy vấn trạng thái dịch vụ
    if not service:
        CloseServiceHandle(scm)
        raise Exception("Mở dịch vụ thất bại")

    # Xóa dịch vụ
    result = DeleteService(service)

    if not result:
        CloseServiceHandle(service)
        CloseServiceHandle(scm)
        raise Exception("Xóa dịch vụ thất bại")

    CloseServiceHandle(service)
    CloseServiceHandle(scm)
    print(f"Dịch vụ '{service_name}' đã được xóa.")

if __name__ == "__main__":
    # Tạo dịch vụ
    create_service("MyService", r"C:\Path\To\Your\Executable.exe", "My Service")

    # Cập nhật dịch vụ (tùy chọn)
    update_service("MyService", start_type=SERVICE_DEMAND_START)  

    # Xóa dịch vụ (tùy chọn)
    # delete_service("MyPythonService")
