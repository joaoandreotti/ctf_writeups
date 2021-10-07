import hashlib

wordlist = open('rockyou.txt', 'r')
hashlist = open('pass.hash', 'r')
for p in wordlist:
	h = hashlib.new('md5')
	h.update(p.encode())
	for l in hashlist:
		if l == h.hexdigest():
			print("FOUND IT:")
			print(p)
