from os.path import realpath
import sys

from pyspark import SparkConf, SparkContext

def pair(a):
	print a
	return (a[0]+a[1])
	

conf = SparkConf()
conf.setMaster("local[4]")
conf.setAppName("damu1000")
conf.set("spark.executor.memory", "4g")

sc = SparkContext(conf=conf)
lines = sc.textFile("damulog.log")


#aa=lines.flatMap(lambda line: line.split(" ")).map(lambda w :(w,1))#.reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], False)

wordlist =lines.flatMap(lambda line: line.split(" "))
f  = sc.parallelize(wordlist.take(1))
l  = sc.parallelize(wordlist.top(1))
print wordlist.collect()
print f.collect()
print l.collect()
print wordlist.subtract(l).collect()
print wordlist.subtract(f).collect()

#print wordlist.subtract(l).zip(wordlist.subtract(f)).collect()

"""
secondwordlist = wordlist.subtract(f)	#remove first element


wordlist = wordlist.subtract(l)

print f.collect()
print l.collect()
print wordlist.collect()
print secondwordlist.collect()

"""

#print wordlist.map(lambda w :(w,1)).reduceByKey(lambda x,y: x+y).collect()
#print wordlist.take(1)
#wordlist =  wordlist.zipWithIndex()


#print wordlist.map(pair).collect()
#print wordlist.collect()
"""
#firstwordlist = ["dummy"] + wordlist.collect()
#wordlist = wordlist.collect() + ["dummy"]

wordlist = ["dummy"] + wordlist;

wordlist = sc.parallelize(wordlist)
firstwordlist = sc.parallelize(firstwordlist)

wordlist =  firstwordlist.zip(wordlist)

print wordlist.map(lambda w :(w,1)).reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], False).take(10)#.collect()


for line in firstwordlist.take(100):
    print line
	
"""

	