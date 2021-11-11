import csv
from k_means import *
from rescale import *

def readDataFromCSV(filename):
  
  csv_file = open(filename, 'r')
  csv_reader = csv.DictReader(csv_file, delimiter = ';')

  data = []

  for row in csv_reader:
    if row['Year'] != '' and row['Number of victims'] != '' and row['Location start'] != '':
      if int(row['Number of victims']) < 997:
        data.append(list(map(int, [row['Year'], row['Number of victims'], row['Location start']])))

  
  return data