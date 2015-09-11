import math

count = 3
prime=[2]

while count <= 1000000000000000000000000003192130093227:
	isprime = True
	sq = int(math.sqrt(count) + 1)
	for x in prime:
		if x > sq:
			break
		if count % x == 0: 
			isprime = False
			break

	if isprime:
		 #return count
		 prime.append(count)
		 print count
	
	count += 2

#print prime