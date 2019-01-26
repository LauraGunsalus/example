from example import algs
import time
import numpy as np
import matplotlib.pyplot as plt

#################################
# Functions
#################################

# Generate random vectors and run sorting algorithms
def getSortTime(sortFun, vectorSize, vectorNumber):
	randomVecs = [np.random.random(vectorSize) for i in range(vectorNumber)]
	startTime = time.time()
	totalVecs = list(map(sortFun, randomVecs))
	sortedVecs, assigns, conds = list(zip(*totalVecs))
	endTime = time.time()
	runTime = endTime - startTime
	return runTime, list(assigns), list(conds)

# Generate vectors of given size
def generateData(sortFun, maxVectorSize, vectorNumber):
	lengths = []
	conditionals = []
	assignments = []
	times = []
	for vectorLength in range(0,1100,100):
		quickTime, quickA, quickC = getSortTime(sortFun, vectorLength, vectorNumber)
		lengths += ([vectorLength] * vectorNumber)
		conditionals += quickC
		assignments += quickA
		times.append(quickTime)
	return(lengths, conditionals, assignments, times)

# Generate plots 
def plotComplexity(xaxis, yaxis, ylabel, type, title, c=1):
	plt.scatter(xaxis,yaxis)
	plt.xlabel("Vector Length")
	plt.ylabel(ylabel)
	if (type == "n_squared"):
		squared = [(i ** 2) * c for i in xaxis]
		plt.plot(xaxis, squared, label = '$n^2$')
	elif (type == "nlogn"):
		nlogn = [i * np.log(i) * c for i in xaxis]
		plt.plot(xaxis, nlogn, label = '$nlog(n)$')
		plt.yscale("log")
	plt.legend(loc='best')
	plt.title(title)
	plt.show()

#################################
# Plot
#################################

# Generate Data for Quicksort
(qlengths, qconditionals, qassignments, qtimes) = generateData(algs.quicksort, 1000, 100)

# Plot Quicksort
plotComplexity(qlengths, qconditionals, "Number of Conditionals", "nlogn", "Quicksort Conditionals",2)
plotComplexity(qlengths, qassignments, "Number of Assignments", "nlogn", "Quicksort Assignments", 5)
plotComplexity(list(range(0,1100,100)), qtimes, "Time (seconds)", "nlogn", "Quicksort Runtime", 0.00009)

# Generate Data for Bubblesort
(blengths, bconditionals, bassignments, btimes) = generateData(algs.bubblesort, 1100, 100)

# Plot Bubblesort
plotComplexity(blengths, bconditionals, "Number of Conditionals", "n_squared", "Bubblesort Conditionals", 0.5)
plotComplexity(blengths, bassignments, "Number of Assignments", "n_squared", "Bubblesort Assignments", 0.5)
plotComplexity(list(range(0,1100,100)), btimes, "Time (seconds)", "n_squared", "Bubblesort Runtime", 0.0000195)

