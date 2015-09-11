import sys
state=[]
x = 0
y = 0
def rc4init(key):
	global state
	i=255
	
	while i>=0:		#initialize state array
		state.append(i)
		i=i-1
	
	i = 0
	j = 0
	while i<256:
		t = state[i]
		j = (j + key[j] + t)%256		#error 1 - it should be j, not k #another mistake - if we do not do "mod 256", then index will run out of bound. checked wiki to confirm. It does "mod" in algo
		state[i] = state[j]
		state[j] = t
		i=i+1
		j=(j+1)%len(key)
		

def rc4_next_octate():
	global x
	global y
	global state
	x = (x + 1)%256
	y = (y + state[x])%256	#another mistake - if we do not do "mod 256", then index will run out of bound. checked wiki to confirm. It does "mod" in algo
	t=state[y]
	state[y]=state[x]
	state[x]=t
	return (state[(state[x] + state[y])%256])
		

#take input key and plain text
key = raw_input("Enter Key:")
key = map(ord,key)
print key
		
plain_text = raw_input("Enter Plain text:")
plain_text = list(plain_text)
rc4init(key)


#ignore first 512 octates
for i in range(0,512):
	rc4_next_octate()
	
cipher=bytearray()
for l in plain_text:
	i = rc4_next_octate()
	#print l + "\t%d\t%d" % (i, (ord(l) ^ i))
	cipher.append(ord(l) ^ i)

print cipher
	
