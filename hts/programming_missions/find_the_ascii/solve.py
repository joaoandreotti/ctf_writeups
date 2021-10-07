from PIL import Image
img = Image.open ('PNG')

y = 0
dst = 0
morse = {
        '.-' : 'a',
        '-...' : 'b',
        '-.-.' : 'c',
        '-..' : 'd',
        '.' : 'e',
        '..-.' : 'f',
        '--.' : 'g',
        '....' : 'h',
        '..' : 'i',
        '.---' : 'j',
        '-.-' : 'k',
        '.-..' : 'l',
        '--' : 'm',
        '-.' : 'n',
        '---' : 'o',
        '.--.' : 'p',
        '--.-' : 'q',
        '.-.' : 'r',
        '...' : 's',
        '-' : 't',
        '..-' : 'u',
        '...-' : 'v',
        '.--' : 'w',
        '-..-' : 'x',
        '-.--' : 'y',
        '--..' : 'z',
        '-----' : '0',
        '.----' : '1',
        '..---' : '2',
        '...--' : '3',
        '....-' : '4',
        '.....' : '5',
        '-....' : '6',
        '--...' : '7',
        '---..' : '8',
        '----.' : '9'
}
letter = ''
while True:
    try:
        for x in range (0, 100):
            if img.getpixel ((x, y)) != 0:
                if chr (dst) == ' ':
                    print (morse [letter], end='')
                    letter = ''
                else:
                    letter += chr (dst)
                dst = 0
            dst += 1
        y += 1
    except:
        print ()
        break
