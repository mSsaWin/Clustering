from functools import reduce
import math
from copy import deepcopy

def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    return reduce(vector_add, vectors)

def sum_of_squares(v):
    return dot(v, v)

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
   return math.sqrt(squared_distance(v, w))

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def mean(x): # среднее значение
  return sum(x)/len(x)

def de_mean(x): # отклонения от среднего
  return [x_i - mean(x) for x_i in x]

def variance(x) : # дисперсия
  return sum_of_squares(de_mean(x))/(len(x)-1)

def standard_deviation(x): # стандартное отклонение
  return math.sqrt(variance(x))