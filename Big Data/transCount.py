from pyspark import SparkConf
from pyspark import SparkContext
conf = SparkConf()
conf.setMaster("local[4]")
conf.setAppName("reduce")
conf.set("spark.executor.memory", "4g")

def splitLine (lines):
	words = lines.split(" ")
	iterator = iter(words)
	prevword = next(iterator)
	array = []
	for word in iterator:
	    array.append("("+prevword+","+word+")")
	    prevword = word
	return array


sc = SparkContext(conf=conf)

lines = sc.textFile("sherlock.txt")
counts = lines.flatMap(splitLine) \
			.map(lambda word: (word,1)) \
			.reduceByKey(lambda x,y: x+y) \
			.sortBy(lambda x: x[1], False) \
			.take (10)

print (counts)
#output = counts.collect()

# for (word, count) in output:
#      print("%s: %i" % (word, count))