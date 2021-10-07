from pwn import *
import time
import os
import signal

ans = "jbgkfmgkknbiblpmibgkcneiedgokibmekffokamknbkhgnlhnajeefpekiefmjgeogjbflijnekebeokpgngjnfbimlkdjdjhan"
elem = ['0', '1', '2', '3', '4', '5', '6' ,'7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

comp = process ('gcc decompiled.c', shell=True)

flag = ''
while (len (flag) < 100):
    for i in elem:
        otp = process ('./a.out ' + flag + i, shell=True)
        x = str (otp.read ())[2:len (flag) + 3]
        otp.close ()
        if ans [0:len (flag) + 1] == x:
            flag = flag + i
            break
    print (flag)

to_xor = 'b4cbb83d4a7f83550fd73ec65ff938a736bda45a4a5fb08311afbef1fc42d48945062661b3d76dd4358ef91c5d16cc0104b3'
for i in range (0, 100, 2):
    a = int ('0x' + flag [i: i + 2], 16)
    b = int ('0x' + to_xor [i: i + 2], 16)
    print (chr (a ^ b), end = '')
