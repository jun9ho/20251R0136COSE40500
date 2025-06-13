# System call simulation using function dispatcher

def sys_write(message):
    print(f"[write] {message}")

def sys_add(a, b):
    return a + b

def sys_exit():
    print("[exit] Program terminated")

system_calls = {
    1: sys_write,
    2: sys_add,
    3: sys_exit
}

def syscall(call_number, *args):
    if call_number in system_calls:
        return system_calls[call_number](*args)
    else:
        print(f"[error] Invalid system call: {call_number}")

syscall(1, "Hello from system call!")
print(f"[add result] {syscall(2, 5, 3)}")
syscall(3)
