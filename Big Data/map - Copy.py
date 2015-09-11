from os.path import realpath
import sys

from pyspark import SparkConf, SparkContext

conf = SparkConf()
conf.setMaster("local[4]")
conf.setAppName("damu1000")
conf.set("spark.executor.memory", "4g")

sc = SparkContext(conf=conf)
lines = sc.textFile("big.txt")


#aa=lines.flatMap(lambda line: line.split(" ")).map(lambda w :(w,1))#.reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], False)

wordlist =lines.flatMap(lambda line: line.split(" "))

firstwordlist = ["dummy"] + wordlist.collect()
wordlist = wordlist.collect() + ["dummy"]

wordlist = sc.parallelize(wordlist)
firstwordlist = sc.parallelize(firstwordlist)

wordlist =  firstwordlist.zip(wordlist)

print wordlist.map(lambda w :(w,1)).reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], False).take(10)#.collect()

"""
for line in firstwordlist.take(100):
    print line
	
"""