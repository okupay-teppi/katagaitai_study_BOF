#!/usr/bin/python3
#-*-coding:utf-8-*-

from pwn import *

target = process("./chall")

# address
libc_binsh_off = 
libc_system_off =
libc_base_addr = 

libc_system_addr = 
libc_binsh_addr = 

print("system : 0x{:x}".format(libc_system_addr))
print("/bin/sh : 0x{:x}".format(libc_binsh_addr))

# payload
payload = b"A" * 
payload +=


target.sendline(payload)

target.interactive()
