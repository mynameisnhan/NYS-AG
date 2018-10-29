import pandas as pd

### -------------------
### DATA PRE-PROCESSING 1.
### Drop duplicate rows, drop empty columns, drop rows with null dates and county codes.
### -------------------


def drop(inpath):

    # Create data frame
    print("Creating data frame...")
    df = pd.read_csv(inpath) # Newest Cases.csv file
    print("Input size: ", df.shape)

    # Drop completely empty columns
    print("Dropping completely empty columns...")
    df = df.dropna(axis = 'columns', how = 'all')

    # Drop irrelevant columns
    print("Dropping pk_id and cas1complexity columns...")
    df = df.drop('pk_id', axis = 1) # Index number generated during exporting Cases to csv
    df = df.drop('cas1complexity', 1) # Case complexity not known at beginning of case
    print("Post-drop size: " + str(df.shape))

    # Rename rows
    df = df.rename(columns = {'cas1idxno': 'index_no'})
    df = df.rename(columns = {'cas1cnty': 'county_code'})

    # Drop completely duplicate rows
    print("Dropping completely duplicate rows...")
    df = df.drop_duplicates()

    # Drop duplicate entries in each county
    print("Dropping duplicate entries in each county...")
    df = df.drop_duplicates(['county_code', 'index_no'])

    # Drop index_no column
    print("Dropping index column...")
    df = df.drop('index_no', 1)
    print("Post-drop size: " + str(df.shape))

    # Drop columns with missing values for county_code, cas1rjidat (case start date), and cas1dispdat (disposition date)
    print("Dropping rows with missing county codes, case start dates, and disposition dates...")
    df = df.dropna(axis = 1, how = 'all')
    df = df.dropna(subset = ['county_code'])
    df = df.dropna(subset = ['cas1rjidat'])
    df = df.dropna(subset = ['cas1dispdat'])

    print("Post-drop size: " + str(df.shape))

    # Output to csv
    # df.to_csv(outpath, index=False)

    return df