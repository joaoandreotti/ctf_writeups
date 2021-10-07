cipher = 'ynkooejcpdanqxeykjrbdofgkq'
for j in range (0, 27):
    print (str (j) + ' : ', end='')
    for i in range (0, len (cipher)):
        print (chr (((ord (cipher [i]) - j) % 26) + ord ('a')), end='')
    print()
