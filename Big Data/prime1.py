import math
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf()
conf.setMaster("local[4]")
conf.setAppName("damu1000")
conf.set("spark.executor.memory", "4g")
sc = SparkContext(conf=conf)

count = 3
prime=[2]

#A=Range(3,1000000000000000000000000003192130093227)
A = range(3,50)
pA=sc.parallelize(A)

prime = pA.map(lambda x: for x in prime)

while count in pA:
	isprime = True

	for x in prime:
		if x > int(math.sqrt(count) + 1):
			break
		if count % x == 0: 
			isprime = False
			break

	if isprime:
		 #return count
		 prime.append(count)
		 print count
		
count += 2

print prime

