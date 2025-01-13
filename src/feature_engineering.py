import pandas as pd

def feature_engineering(df):
    # create time features
    df['day_of_week'] = df.index.dayofweek
    df['month'] = df.index.month
    df['quarter'] = df.index.quarter
    df['year'] = df.index.year
    df['day_of_year'] = df.index.dayofyear
    # make ordinal
    df['date'] = df.index
    df['ordinal'] = df['date'].apply(lambda x: x.toordinal())
    # drop date
    df.drop('date', axis=1, inplace=True)

    time_columns = ['month', 'quarter', 'day_of_week', 'day_of_year','year','ordinal']

    #print('feature engineering done!')
    return df