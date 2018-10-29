import pandas as pd
import numpy as np
import os
import DataProc1 as dp1
import DataProc2 as dp2
import DataProc3 as dp3
import DataProc4 as dp4
import Model

def DataProc(inpath):
    train = dp1.drop(inpath)
    train = dp2.drop_bad_date(train)
    train = dp2.standardize(train)
    train = dp3.clean(train)
    train, test, validation =  dp3.split(train) # Use d_split instead of split to generate sets of half size (with 30/10/10 split instead of 60/20/20 split)
    train, y_train = dp4.one_hot_encode(train)
    test, y_test = dp4.one_hot_encode(test)
    validation, y_validation = dp4.one_hot_encode(validation)

    return train, y_train, test, y_test, validation, y_validation

DataProc("Cases.csv")
Model()