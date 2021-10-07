from PIL import Image

img = Image.open ("4202252.jpg")

msg = ''

p = img.load ()

print ("[*] Starting")
for i in range (0, img.width):
    r, g, b = p [i, 0]
    msg += format (r, 'b')[len (format (r, 'b')) - 1]
    msg += format (g, 'b')[len (format (g, 'b')) - 1]
    msg += format (b, 'b')[len (format (b, 'b')) - 1]

print (msg)

ans = []
for i in range (0, len (msg) // 8)
    b = msg [i * 8:(i + 1) * 8][::-1]
    ans.append (chr (int  (''.join ([str (bit) for bit in b]), 2)))

print (ans)
