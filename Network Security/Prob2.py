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
		
		
def leftshift(text):
	msb = text & 0x80
	text = text & 0x7f	#remove msb
	text = text << 1
	msb = msb >> 7		#make msb as lsb
	return (text | msb)
	

#take input key and plain text
key = raw_input("Enter Key:")
key = map(ord,key)
print key
		
plain_text = raw_input("Enter Plain text:")
plain_text = list(plain_text)


i=255

while i>=0:		#initialize state array
	state.append(i)
	i=i-1
	
substitution=[]

for i in range(0,8):		#generate 8 substitution tables using RC4
	rc4init(key)
	substitution.append(state)

#print substitution

cipher=map(ord,plain_text)

for i in range(0,16):		#16 times rotation
	j=0
	for l in cipher:
		#print "original: "+l
		l = l ^ key[j]	#xor with key
		#print "xor: %d, %d"%(i%8,l)
		l = substitution[i%8][l]	#substitution - doing i%8 as we have only 8 tables, but loop runs for 16 times
		#print "substitution: %d"%l
		l = leftshift(l)
		#print "leftshift: %d"%l
		cipher[j]=l
		j = j + 1
print cipher


