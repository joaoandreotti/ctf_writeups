cipher = 'UFJKXQZQUNB'
key = 'SOLVECRYPTO'

for i in range (0, len (key)):
    print (chr (ord ('A') + (ord (cipher [i]) - ord (key [i])) % 26), end = '')
