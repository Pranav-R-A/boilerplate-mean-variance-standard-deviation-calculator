import numpy as np

def calculate(list):
    if(len(list)<9):
        raise ValueError("List must contain nine numbers.")
    newList = np.array([list[0:3], list[3:6], list[6:]])
    calculations = {"mean": [np.average(newList, 0).tolist(), np.average(newList, 1).tolist(), np.average(newList)],
                    "variance": [np.var(newList, 0).tolist(), np.var(newList, 1).tolist(), np.var(newList)],
                    "standard deviation": [np.std(newList, 0).tolist(), np.std(newList, 1).tolist(), np.std(newList)],
                    "max": [np.max(newList, 0).tolist(), np.max(newList, 1).tolist(), np.max(newList)],
                    "min": [np.min(newList, 0).tolist(), np.min(newList, 1).tolist(), np.min(newList)],
                    "sum": [np.sum(newList, 0).tolist(), np.sum(newList, 1).tolist(), np.sum(newList)]}
    return calculations