from os.path import realpath
import sys
from pyspark import SparkConf, SparkContext
from math import pow
#http://www.numberempire.com/primenumbers.php
#1000000000000000000000000003192130093191*1000000000000000000000000003192130093227


a=1000000000000000000000000003192130093191*1000000000000000000000000003192130093227

print 6%2


""""
conf = SparkConf()
conf.setMaster("local[4]")
conf.setAppName("damu1000")
conf.set("spark.executor.memory", "4g")

print "Damu"

sc = SparkContext(conf=conf)
A = range(1000)
pA=sc.parallelize(A)
sum=pA.map(sqrt).reduce(lambda a,b: a+b)
print sum
"""
