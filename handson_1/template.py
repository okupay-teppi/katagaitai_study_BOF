#!/usr/bin/python3
#-*-coding:utf-8-*-

from pwn import *


target = process('./handson_1')

secret = 

payload = b"A" * 
payload += p32()

target.sendline(payload)

print(target.recvline())

# target.interactive()
