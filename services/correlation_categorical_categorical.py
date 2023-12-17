import numpy as np
import pandas as pd
import scipy as sc


def correlation_categorical_categorical(categories_1, categories_2):
    chi2 = sc.stats.chi2_contingency(pd.crosstab(categories_1, categories_2))[0]
    n = pd.crosstab(categories_1, categories_2).to_numpy().sum()
    phi2 = chi2/n
    r, k = pd.crosstab(categories_1, categories_2).shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min( (kcorr-1), (rcorr-1)))