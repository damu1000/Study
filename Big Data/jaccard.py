from os.path import realpath
import sys
from pyspark import SparkConf, SparkContext
#import numpy as np
#import matplotlib.pyplot as plt

#c if rdd can be passed / data type declared for function arg
def myprint(a):
	#print a[1].split(" ")
	return a[0],list(set(a[1].split(" ")))
	
def compare_books(pair):
	return pair[0][0],pair[1][0],float(len(set(pair[0][1]) & set(pair[1][1]))) / len(set(pair[0][1]) | set(pair[1][1]))

		

conf = SparkConf()
conf.setMaster("local[4]")
conf.setAppName("damu1000")
conf.set("spark.executor.memory", "4g")

sc = SparkContext(conf=conf)

books = sc.wholeTextFiles(".\\Test\\*.txt")
print "reading files completed"
booknames = books.map(lambda (x,y):(x)).collect()
print booknames[0]

filelist = []
for i in range(0, len(booknames)):
	for j in range(i+1,len(booknames) ):
		filelist.append((booknames[i],booknames[j]))
#print filelist

books = books.map(myprint)		#simpler way is (copied from canvas)- print books.map(lambda (x,y): (x,y.split(" ")) ).collect()
print "word split completed"
books = books.cartesian(books)	#each tuple is one book pair
print "cartesian prouct completed"

books = books.filter(lambda (x,y):(x[0],y[0]) in filelist)	# eliminate self comparison
#print books.collect()
result = books.map(compare_books)
print "saving output"
result.saveAsTextFile(".\\Test\\result.txt")
#print result.collect()

#values = result.values().collect()
#plt.hist(values, 256, range=(0.0,1.0), fc='k', ec='k')
#plt.show()


