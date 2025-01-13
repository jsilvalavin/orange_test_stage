# imports
import pandas as pd
import numpy as np
import os

def data_processing():
    # set path
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../data/telecom_sales_data.csv')

    # read data
    df = pd.read_csv(filename)

    # set datetime index
    df.rename(columns={'Unnamed: 0': 'date'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    # for ease of use
    jphone = 'jPhone_Pro_revenue'
    kaggle = 'Kaggle_Pixel_5_revenue'
    planet = 'Planet_SX_revenue'

    # remove nan errors
    df['tech_event'] = df['tech_event'].fillna('')

    # trasformation of cathegorical variables
    dict_cath = {'Bad': 0, 'Good': 1, 'Moderate': 2,
                '': 0, 'Tech Show': 1, 'Major Launch': 2,
                'Pre-5G': 0, 'Early-5G': 1, 'Mid-5G': 2, 'Mature-5G': 3,
                'Poor': 0, 'Limited': 1, 'Good': 2, 'Hub': 3}

    df = df.replace(dict_cath)
    #print('Data processing done!')
    return df