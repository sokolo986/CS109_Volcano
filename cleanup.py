import pandas as pd
from datetime import datetime
from sklearn.preprocessing import Imputer
import numpy as np
import astropy.time

def convert_dates(df, year_col, month_col, day_col):
    #python datetime does not support dates before 1AD. There is a python module called datautil we can use if necessary
    #np.nan only works with floats...Start Years are ints and there are no NaN values,
    #but End Years are floats with NaN's 
    column = df.apply(lambda row: np.nan if ( (np.isnan(float(row[year_col]))) | (np.isnan(float(row[month_col]))) | (np.isnan(float(row[day_col])))\
                        | (float(row[month_col]) == 0) | (float(row[day_col]) == 0))\
                        else datetime(int(row[year_col]), int(row[month_col]), int(row[day_col])) , axis=1)
    return column
	
def convert_zero(df, column, value):
    zero_days = df[df[column]==0].index
	
    for i in zero_days:
        df.ix[i,column]=value
    return df

def eliminate_nan(df, column):
    new_df = df[df[column].notnull()]
    return new_df

def julian_date(df, date_col):
    column = astropy.time.Time(df[date_col],scale='tai').jd
    return column

def mean_days(df, start_col, end_col):
    mean = np.sum(df[end_col]-df[start_col])/float(len(df))
    return mean

def impute_vei(df, col):
    array = df.as_matrix([col])
    imp = Imputer(missing_values = 'NaN', strategy = 'most_frequent', axis = 0)
    new_array = imp.fit_transform(array)
    return new_array

#def impute_erup_length(df, start_date_col, end_date_col):
	
	
