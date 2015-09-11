from numpy import array
from numpy.linalg import norm 
from os.path import realpath
import sys
from pyspark import SparkConf, SparkContext

#c if rdd can be passed / data type declared for function arg
def myprint(a):
	return a[0],a[1].split(" ")
	
def compare_books(pair):
	return pair[0][0],pair[1][0],float(len(set(pair[0][1]) & set(pair[1][1]))) / len(set(pair[0][1]) | set(pair[1][1]))

def dotproduct(vector1, vector2):
  return sum((i*j) for i, j in zip(vector1, vector2))

def custom_filter(y, cw):
	newlist = []
	i=0
	for word in cw:
		newlist.append(y.count(word))
	return newlist


conf = SparkConf()
conf.setMaster("local[4]")
conf.setAppName("damu1000")
conf.set("spark.executor.memory", "4g")

sc = SparkContext(conf=conf)

books = sc.wholeTextFiles(".\\Test\\*.txt")
print "reading files completed"

allwords = books.flatMap(lambda (x,y): y.split(" "))
allwords1 = allwords.map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], False).take(1000)	#list of most common_words
featured_vector = map(lambda (x,y): y, allwords1)	#featured_vector
common_words = map(lambda (x,y): x, allwords1)		#most common words

books = books.map(lambda (x,y): (x,y.split(" ") ))
books = books.map(lambda (x,y): (x, custom_filter(y, common_words) ))		#split words inside book and filter for common words only along with counts


#prepare list without dups
booknames = books.map(lambda (x,y):(x)).collect()
filelist = []
for i in range(0, len(booknames)):
	for j in range(i+1,len(booknames) ):
		filelist.append((booknames[i],booknames[j]))
#print filelist

books = books.cartesian(books)	#each tuple is one book pair
print "cartesian prouct completed"
books = books.filter(lambda (x,y):(x[0],y[0]) in filelist)	# eliminate self comparison and dups
books = books.map(lambda (x,y): (x[0], y[0], dotproduct((x[1]/norm(x[1])),(y[1]/norm(y[1]))) ) )	#normalize and take dot product
books.saveAsTextFile(".\\Test\\result.txt")

"""
print allwords1
print common_words
print featured_vector
print books.collect()
"""


