import base64

secret = base64.b64decode ('NQALCgEDDDEzUjpTBwocBgcDPTIIGwIK')
key = 'beginning'

ans = ''

for i in range (len (secret)):
    ans = ans + chr (secret [i] ^ ord (key [i % len (key)]))

print (ans)
