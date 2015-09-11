import sys
state=[]
x = 0
y = 0

def rc4init(key):
	global state
	i = 0
	j = 0
	while i<256:
		t = state[i]
		j = (j + key[j] + t)%256		#error 1 - it should be j, not k #another mistake - if we do not do "mod 256", then index will run out of bound. checked wiki to confirm. It does "mod" in algo
		state[i] = state[j]
		state[j] = t
		i=i+1
		j=(j+1)%len(key)
		

		
def rightshif(text):
	lsb = text & 0x01
	text = text >> 1
	lsb = lsb << 7		#make msb as lsb
	return (text | lsb)

def find_index(text, num):
	for i in range(0,256):
		#print text[i]
		if text[i]==num:
			return(i)
	
#take input key and plain text
key = raw_input("Enter Key:")
key = map(ord,key)
print key
		
ip = raw_input("Enter Cipher text:")
ip = ip.split(" ")

plain_text=[]
for ele in ip:
	plain_text.append(int(ele))
	
i=255

while i>=0:		#initialize state array
	state.append(i)
	i=i-1
	

substitution=[]

for i in range(0,8):		#generate 8 substitution tables using RC4
	rc4init(key)
	substitution.append(state)

#print substitution	
	
cipher=plain_text
print cipher

for i in range(0,16):		#16 times rotation
	j=0
	for l in cipher:
		l2 = rightshif(l)
		#print "rightshif: %d"%l2
		

		#print substitution[(15-i)%8]
		l1 = find_index(substitution[(15-i)%8],l2)	#(15-i)%8 -> traversing list from 7 to 0 as i increments from 0 to 15. Index will give the original byte
		#print "substitution: %d"%l
		#print l1
	
		#print "original: "+l
		l = l1 ^ key[j]	#xor with key
		#print "xor: %d, %d"%(i%8,l)
		cipher[j]=l
		j = j + 1

plain_text = map(chr,cipher)
print ''.join(plain_text)


