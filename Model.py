import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

# Select k importances.
def select_k_importances(model, x, k):
    return x[:, model.feature_importances_.argsort()[::-1][:k]]

### -------------------
### TESTING.
### -------------------

'''
x_train = pd.read_csv("d_x_test.csv")
y_train = pd.read_csv("d_y_test.csv", names=['actual'])
x_test = pd.read_csv("d_x_test.csv")
y_test = pd.read_csv("d_y_test.csv", names=['actual'])
'''

def model(x_train, y_train, x_validation, y_validation):
    print(x_train.shape, y_train.shape, x_validation.shape, y_validation.shape)
    scale = MinMaxScaler()
    scale.fit(x_train.values)
    x_train = scale.transform(x_train.values)
    y_train = y_train.values
    rf_y_validation = y_validation
    lr_y_validation = y_validation
    x_validation = x_validation.values
    y_validation = y_validation.values

    # Backward elimination.
    model1 = RandomForestRegressor(n_estimators = 10)
    model1.fit(x_train, y_train)

    n_features =  x_train.shape[1]
    count = 1

    while n_features >= 1:
        x_train = select_k_importances(model1,x_train, n_features)
        x_validation = select_k_importances(model1, x_validation, n_features)

        print(count, n_features)

        # Random forest
        model1 = RandomForestRegressor(n_estimators = 10)
        model1.fit(x_train, y_train)
        temp = model1.score(x_validation, y_validation)
        rf_y_validation[str(n_features)] = model1.predict(x_validation, y_validation)
        print(temp)


        # Linear regression
        model4 = LinearRegression()
        model4.fit(x_train, y_train)
        temp = model4.score(x_validation, y_validation)
        lr_y_validation[str(n_features)] = model1.predict(x_validation, y_validation)
        print(temp)

        n_features -= n_features * .10
        n_features = int(n_features)

        count += 1

        print(lr_y_validation)

# model(x_train, y_train, x_test, y_test)