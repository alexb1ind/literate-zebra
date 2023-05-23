import subprocess

file_names = ["d_linux_amd64", "d_linux_amd64"]  

processes = []
for file_name in file_names:
    command = f"./{file_name}"
    process = subprocess.Popen(command, shell=True)
    processes.append(process)


for process in processes:
    process.wait()