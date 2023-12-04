import numpy as np
import pandas as pd
import scipy as sc


def correlation_categorical_categorical(categories_1, categories_2):
    data = pd.crosstab(categories_1, categories_2)
    return np.sqrt((sc.stats.chi2_contingency(data, correction=True)[0] / data.sum().sum()) / (min(data.shape) - 1))