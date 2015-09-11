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

mat1 = sc.textFile(".\\test\\a_3x3.txt").map(lambda line: line.split(" "))	#dont use flat map as it will remove partition
mat1 = mat1.map(lambda x: ((int(x[0]) ),float(x[2]) )) 	#form key value payer as i , Mij
mat1 = mat1.groupByKey().mapValues(list).sortBy(lambda x: x[0], True)		#got each row as a list along with its index as keys

mat2 = sc.textFile(".\\test\\b_3x3.txt").map(lambda line: line.split(" "))	#dont use flat map as it will remove partition
###########################			V IMP: now we take matrix column (j) and value(Mij) as key value pair. this will give one tuple in RDD as 1 column of matrix 2. Multiplication will be eaiser
mat2 = mat2.map(lambda x: ((int(x[1]) ),float(x[2]) )) 	#form key value payer as j , Mij	
mat2 = mat2.groupByKey().mapValues(list).sortBy(lambda x: x[0], True)		#got each row as a list along with its index as keys


mat = mat1.cartesian(mat2)
prod = mat.map(lambda (x,y): ( int(x[0]), int(y[0]) ,dotprod(x[1],y[1])) ).sortBy(lambda x: x[0], True)	#dot prod of each row from matrix with vector

#print mat1.collect()
#print mat2.collect()
#print prod.collect()
prod.saveAsTextFile(".\\Test\\prod")


