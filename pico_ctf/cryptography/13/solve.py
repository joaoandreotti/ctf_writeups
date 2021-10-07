cipher = 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}'
j = 13
print (str (j) + ' : ', end='')
for i in range (0, len (cipher)):
    if cipher [i] >= 'a' and cipher [i] <= 'z':
        print (chr ((((ord (cipher [i]) - ord ('a')) + j) % 26) + ord ('a')), end='')
    elif cipher [i] >= 'A' and cipher [i] <= 'Z':
        print (chr ((((ord (cipher [i]) - ord ('A')) + j) % 26) + ord ('A')), end='')
    else:
        print (cipher [i], end='')
print()
