words = open ('james', 'r')
wordlist = open ('wordlist.txt', 'r').read ().split ('\n')
ans = ""

for w in words.read ().split ('\n'):
    if w != '\t' and w != '':
        for wl in wordlist:
            #print (w + ' | ' + wl)
            if sorted (w) == sorted (wl):
                if len (ans) > 0:
                    ans += ', ' + wl
                else:
                    ans = wl
print (ans)
