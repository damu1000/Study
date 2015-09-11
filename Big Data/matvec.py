import numpy as np
from numpy.linalg import norm 
from os.path import realpath
import sys
from pyspark import SparkConf, SparkContext

def dotprod(a,b):
	c=0
	j=0
	for i in a:
		c = c + i*b[j]
		j=j+1
	return(c)

conf = SparkConf()
conf.setMaster("local[4]")
conf.setAppName("damu1000")
conf.set("spark.executor.memory", "4g")

sc = SparkContext(conf=conf)

mat = sc.textFile(".\\test\\a_10Kx2K.txt").map(lambda line: line.split(" "))	#dont use flat map as it will remove partition
mat = mat.map(lambda x: ((int(x[0]) ),float(x[2]) )) 	#form key value payer as i , Mij
mat = mat.groupByKey().mapValues(list).sortBy(lambda x: x[0], True)		#got each row as a list along with its index as keys
vec = sc.textFile(".\\test\\x_2K.txt").map(lambda x: float(x.replace("array([",'').replace("])",'').strip())).collect()	#read vector file and convert it to float array
#prod = mat.map(lambda x: ( int(x[0]) ,np.dot(x[1],vec)) )	#dot prod of each row from matrix with vector
prod = mat.map(lambda x: ( int(x[0]) ,dotprod(x[1],vec)) )	#dot prod of each row from matrix with vector

#print mat.collect()
prod.saveAsTextFile(".\\Test\\prod")
