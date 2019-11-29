import matplotlib.pyplot as plt
import random
import math
from numpy import arange


def calculatePi(inCircle, total):
    return 4 * (inCircle / float(total))


def isInCircle(x, y):
    return math.sqrt(x ** 2 + y ** 2) <= 1.0


def plotEstimates(estimates):
    xAxis = arange(1, len(estimates) + 1)
    plt.semilogx(xAxis, estimates)
    plt.xlabel("Number of darts")
    plt.ylabel("Estimate of pi")
    plt.title("Final estimate of pi: {}".format(estimates[-1]))
    plt.axhline(3.14159, color='green')
    plt.show()


def throwDarts(numDarts, shouldPlot):
    inCircle = 0
    estimates = list()
    for darts in range(1, numDarts + 1):
        x = random.random()
        y = random.random()
        if isInCircle(x, y):
            inCircle += 1
        if shouldPlot:
            piGuess = calculatePi(inCircle, darts)
            estimates.append(piGuess)
        if not darts % 10000:
            piGuess = calculatePi(inCircle, darts)
            print("The estimate of pi with {} darts is {}".format(
                darts, piGuess))

    if shouldPlot:
        plotEstimates(estimates)

    return piGuess


def findPi(numDarts, shouldPlot=False):
    piGuess = throwDarts(numDarts, shouldPlot)
    print("Estimated value of pi with {} darts: {}".format(numDarts, piGuess))


if __name__ == '__main__':
    findPi(10000, True)
