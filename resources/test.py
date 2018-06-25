import numpy as np
import pandas as pd
import sklearn
from sklearn.datasets import load_iris
from matplotlib import pyplot as pyplot

from pandas.plotting import scatter_matrix

ds=load_iris()
data = ds.data

x=pd.DataFrame(data,columns = ds.feature_names)
scatter_matrix(x)
