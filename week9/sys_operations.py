import os
import platform
import socket
import sys

print("Current Maachine Type")
print(platform.machine())
print("=====================================")


print("Current Processor Type")
print(platform.processor())
print("=====================================")

print("set socket timeout to 50 seconds")
print(socket.setdefaulttimeout(50))
print("get the current socket timeout")
print(socket.getdefaulttimeout())
print("=====================================")

print("get the current operating system type")
print(os.name)
print("get the current operating system name")
print(platform.system())
print("=====================================")

print("get the current Process ID")
print(os.getpid())
print("=====================================")

file_name = "fdpractice.txt"
print(f"\n[Before Fork] Process {os.getpid()}")
file_handler = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"\n[Process {os.getpid()}] Opened file_handler: {file_handler}")

file_object_TextIO = os.fdopen(file_handler, "w")

file_object_TextIO.write("Some String to write to the file")
file_object_TextIO.flush()

print(f"\n[Before Fork] Process {os.getpid()} Forking now")
pid = os.fork()

if pid == 0:
    # Child Process
    print(f"\n[PID {pid()} has Parent Process ID: {os.getpid}] Process")
    os.lseek(file_handler, 0, 0)

    print(f"[Child Process {os.getpid()}] File Contents: {os.read(file_handler, 100).decode()}")

    os.close(file_handler)
    sys.exit(0)
else:
    print(f"\n[Prent Process ID: {os.getpid()}],  Child PID: {pid}")
    print("wait for the child to complete the execution")
    os.wait()
    print("Child process has completed")
    file_object_TextIO.close()

print(f"\n [Process : {os.getpid()}] file Closed now")
sys.exit(0)
print("=====================================")
    