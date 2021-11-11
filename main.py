from k_means import *
from rescale import *
from csv_reader import *

filename = 'terrorism_events.csv'

inputs = readDataFromCSV(filename)
rescaled_inputs = rescale(inputs)

random.seed(0)
K = 8

clusterer = KMeans(K)
clusterer.train(rescaled_inputs)

print("3 MEANS:")

for mean_clusterer in clusterer.means:
  print(mean_clusterer)

inputs_rows = []

for i in range(K):
  inputs_rows.append([input for input, r_input in zip(inputs, rescaled_inputs) if clusterer.classify(r_input) == i])

fig = plt.figure(figsize=(15,10))

ax = fig.add_subplot(projection = '3d')

for i in range(K):
  ax.scatter([vector[0] for vector in inputs_rows[i]],[vector[1] for vector in inputs_rows[i]],[vector[2] for vector in inputs_rows[i]], label = f'{i+1} cluster')

ax.view_init(45, 50)
plt.xlabel('Year')
plt.ylabel('Number of victims')

plt.legend()

plt.show()