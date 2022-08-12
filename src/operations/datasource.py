from mymodules.operations.ioperator import IOperator
from mymodules.operations.data_operations.datastore import DataStore
import sklearn
from sklearn import datasets
from src.configurations import constants
import pandas as pd
import numpy as np

class DataSource(IOperator):
    def execute():
        wine = sklearn.datasets.load_wine()
        data=pd.DataFrame(data=np.c_[wine['data'],wine['target']],columns=wine['feature_names']+['target'])
        DataStore.store_data(data,constants.NAME_RAW_DATA)
        return
    