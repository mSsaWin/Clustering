import random
from math_func import *
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, k):
        self.k = k         
        self.means = None   

    def classify(self, input):
        return min(range(self.k),
                   key=lambda i: squared_distance(input, self.means[i]))

    def train(self, inputs):

        self.means = random.sample(inputs, self.k)
        assignments = None

        while True:
            new_assignments = list(map(self.classify, inputs))

            if assignments == new_assignments:
                return

            assignments = new_assignments

            for i in range(self.k):
                i_points = [p for p, a in zip(inputs, assignments) if a == i]
                if i_points:
                    self.means[i] = vector_mean(i_points)

def squared_clustering_errors(inputs, k):
    clusterer = KMeans(k)
    clusterer.train(inputs)
    means = clusterer.means
    assignments = list(map(clusterer.classify, inputs))

    return sum(squared_distance(input,means[cluster])
               for input, cluster in zip(inputs, assignments))

def plot_squared_clustering_errors(inputs):

    ks = range(1, 30)
    errors = [squared_clustering_errors(inputs, k) for k in ks]

    plt.plot(ks, errors)
    plt.xticks(ks)
    plt.xlabel("k")
    plt.ylabel("total squared error")
    plt.show()