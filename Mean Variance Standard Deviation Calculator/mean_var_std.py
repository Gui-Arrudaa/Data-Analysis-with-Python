import numpy as np

def calculate(lst):

  if len(lst) < 9:
    raise ValueError('List must contain nine numbers.')

  A = np.array(lst).reshape(3,3)

  mean = [A.mean(axis=0), A.mean(axis=1), A.mean()]
  variance = [A.var(axis=0), A.var(axis=1), A.var()]
  standard_deviation = [A.std(axis=0), A.std(axis=1), A.std()]
  max = [A.max(axis=0), A.max(axis=1), A.max()]
  min = [A.min(axis=0), A.min(axis=1), A.min()]
  sum = [A.sum(axis=0), A.sum(axis=1), A.sum()]

  return {
    'mean': [m.tolist() for m in mean],
    'variance': [v.tolist() for v in variance],
    'standard deviation': [sd.tolist() for sd in standard_deviation],
    'max': [m.tolist() for m in max],
    'min': [m.tolist() for m in min],
    'sum': [s.tolist() for s in sum]
  }
