from datetime import datetime

### -------------------
### DATA PRE-PROCESSING 2.
### Convert dates to datetime, calculate days elapsed, drop old date columns.
### -------------------

# No longer relevant because all dates in new dataset have identical formatting
'''
def val_date1(d):
    try:
        datetime.strptime(str(d), '%m/%d/%Y')
        return True
    except ValueError:
        return False
'''

# Check to see if date is in correct format
def val_date2(d):
    try:
        datetime.strptime(str(d), '%Y%m%d')
        return True

    except ValueError:
        return False

# No longer relevant because all dates in new dataset have identical formatting
'''
def val_date3(d):
    try:
        datetime.strptime(str(d), '%m-%d-%Y')
        return True
    except ValueError:
        return False
'''

# Drop dates that are 0 or do not have 8 digits.
def drop_bad_date(df):
    print("Dropping dates with 0 values and dates with less than or more than 8 digits...")
    df = df[df.cas1rjidat != 0]
    df = df[df.cas1dispdat != 0]
    df = df[df.cas1dispdat > 9999999]
    df = df[df.cas1rjidat > 9999999]
    df = df[df.cas1dispdat < 100000000]
    df = df[df.cas1rjidat < 100000000]
    print("Post-drop size: " + str(df.shape))

    return df

# Standardize dates to datetime format and find days elapsed between cas1rjidat (case start date) and cas1dispdat (disposition date)
def standardize(df):
    # inval_drop_count = 0
    # neg_drop_count = 0

    print("Calculating days elapsed for row 1.")
    for i, row in df.iterrows():

        # Drop row if dates are not in correct format
        if val_date2(row['cas1dispdat']) == False or val_date2(row['cas1rjidat']) == False:
            df.drop(i, inplace=True)
            # inval_drop_count += 1

        # If dates are in correct format...
        else:
            row['cas1rjidat'] = datetime.strptime(str(row['cas1rjidat']), '%Y%m%d')
            row['cas1dispdat'] = datetime.strptime(str(row['cas1dispdat']), '%Y%m%d')

            # Calculate days elapsed
            # Formula: cas1dispdat - cas1rjidat
            # Store info in cas1dispdat column
            row['cas1dispdat'] = (row['cas1dispdat'] - row['cas1rjidat']).days
            df['cas1dispdat'][i] = row['cas1dispdat']

            # Drop row if days elapsed is negative
            if row['cas1dispdat'] < 0:
                df.drop(i, inplace=True)
                # neg_drop_count += 1

    # Drop cas1rjidat column
    print("Dropping cas1rjidat column...")
    df = df.drop("cas1rjidat", axis=1)
    print("Post-drop size: " + str(df.shape))

    # df.to_csv(outpath, index=False)

    return df