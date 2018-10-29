import pandas as pd

### -------------------
### DATA PRE-PROCESSING 3.
### Drop insignificant columns, standardize bad values for all columns, and create train, test, and validation sets.
### -------------------

# Load file.
'''
dated = "dated.csv"

df = pd.read_csv(dated)
print("Input size: ", df.shape)
'''

def clean(df):
    # Remove the following columns, which were determined to be too sparse during exploratory analysis in Explore.ipynb
    remove_columns = ['cas1325sudamt', 'cas1assmtamt', 'cas1iasjust']
    for variable in remove_columns:
        print("Dropping " +  variable + " column...")
        df = df.drop(variable, axis  =1)

    # Remove spaces at end of values for all values
    for variable in df.columns:
        print("Dropping spaces at end of values for  " +  variable + " column...")
        df[variable] = df[variable].apply(lambda x: " ".join(str(x).split()))

    # Remove all rows where the following columns have null values
    remove_row_when_null = ['county_code', 'cas1actntyp', 'cas1damages', 'cas1genlprf', 'cas1rjitji' , 'cas1iascatg','cas1atyctr', 'cas1court', 'car1specprf', 'cas1jscod']
    for variable in remove_row_when_null:
        print("Dropping rows with null values at " + variable + " column...")
        df = df[df[variable] != '']
        df = df[df[variable] != 'nan']

    print("Post-drop size: " + str(df.shape))

    # Write blanks for factorization when the row column is blank or null
    replace_blank_or_null = ['cas1prose', 'cas1efiled', 'cas1munid',  'cas1privatecase']
    for variable in replace_blank_or_null:
        print("Replacing null values with N at " + variable + " column...")
        df[variable][df[variable] == ''] = "N"
        df[variable][df[variable] == 'nan'] = "N"
        df[variable][df[variable] is None] = "N"

    replace_blank_or_null = ['cas1jscod']
    for variable in replace_blank_or_null:
        print("Replacing null values with 0 at " + variable + " column...")
        df[variable][df[variable] == ''] = 0
        df[variable][df[variable] == 'nan'] = 0
        df[variable][df[variable] is None] = 0

    # df.to_csv(outpath, index=False)

    print("Complete unencoded shape: " + str(df.shape))

    return df


# Create training, testing and validation sets 60/20/20
def split(df):
    print("Generating train set...")
    train = df.sample(frac=0.6)
    test = df.drop(train.index)

    print("Generating validation set...")
    validation = test.sample(frac=0.5)

    print("Generating test set...")
    test = test.drop(validation.index)

    train.to_csv('train-unencoded.csv', index=False)
    test.to_csv('test-unencoded.csv', index=False)
    validation.to_csv('validation-unencoded.csv', index=False)

    return train, test, validation

# This was to generate small datasets to test code functionality
def d_split(df):
    train = df.sample(frac=0.5)

    print("Generating train set...")
    d_train = train.sample(frac = 0.6)
    d_test = train.drop(d_train.index)

    print("Generating validation set...")
    d_validation = d_test.sample(frac = 0.5)

    print("Generating test set...")
    d_test = d_test.drop(d_validation.index)

    d_train.to_csv('train-unencoded.csv', index=False)
    d_test.to_csv('test-unencoded.csv', index=False)
    d_validation.to_csv('validation-unencoded.csv', index=False)

    return d_train, d_test, d_validation