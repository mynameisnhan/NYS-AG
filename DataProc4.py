import pandas as pd

### -------------------
### DATA PRE-PROCESSING 4.
### One-hot encode categorical variables.
### -------------------


def one_hot_encode(df):
    # Perform one-hot encoding for categorical variables
    ohe_feats = ['cas1actntyp', 'cas1iascatg', "county_code", 'car1specprf', 'cas1rjitji', 'cas1prose', 'cas1efiled', 'cas1privatecase','cas1jscod', 'cas1genlprf', 'cas1munid', 'cas1damages']
    for f in ohe_feats:
        print("Performing one-hot encoding for " + f + " column...")
        df_dummy = pd.get_dummies(df[f], prefix=f)
        df = df.drop([f], axis=1)
        df = pd.concat([df, df_dummy], axis=1)

    # Split into x and y
    print("Splitting " + str(df) + " into x and y...")
    y_part = df['cas1dispdat']
    x_part = df.drop('cas1dispdat', axis= 1)

    x_part.to_csv("x_" + str(df) + ".csv", index=False)
    y_part.to_csv("y_" + str(df) + ".csv", index=False, names=["actual"])

    return x_part, y_part