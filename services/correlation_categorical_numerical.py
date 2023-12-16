import numpy as np


def correlation_categorical_numerical(categorical, numerical):
    categorical = np.array(categorical)
    numerical = np.array(numerical)
    ssw = 0
    ssb = 0
    for category in set(categorical):
        subgroup = numerical[np.where(categorical == category)[0]]
        ssw += sum((subgroup - np.mean(subgroup)) ** 2)
        ssb += len(subgroup) * (np.mean(subgroup) - np.mean(numerical)) ** 2
    return (ssb / (ssb + ssw)) ** .5