from os.path import realpath
import sys
from pyspark import SparkConf, SparkContext

def myprint(a):
	#print a[1].split(" ")
	return a[0],a[1].split(" ")
	
def compare_books(pair):
	return pair[0][0],pair[1][0],float(len(set(pair[0][1]) & set(pair[1][1]))) / len(set(pair[0][1]) | set(pair[1][1]))
	

conf = SparkConf()
conf.setMaster("local[4]")
conf.setAppName("damu1000")
conf.set("spark.executor.memory", "4g")

sc = SparkContext(conf=conf)

books = sc.wholeTextFiles("C:\\Damu\\Study\\Big Data\\Test\\f*.txt")
books = books.map(myprint)		#simpler way is (copied from canvas)- print books.map(lambda (x,y): (x,y.split(" ")) ).collect()
books = books.cartesian(books)	#each tuple is one book pair
print books.map(compare_books).collect()

#print books.collect()



#prod=books.cartesian(books)
#books.saveAsTextFile("C:\Damu\Study\Big Data\Test\result.txt")
#print books.collect();

#print books.keys().collect()
