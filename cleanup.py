import pandas as pd
from sklearn.preprocessing import Imputer
from datetime import datetime

def convert_dates(df, year_col, month_col, day_col, new_col_name):
    df[new_col_name] = df.apply(lambda row: datetime(int(row[year_col]), int(row[month_col]), int(row[day_col])), axis=1)
    return df

def convert_zero(df, column):
    zero_days = df[df[column]==0].index
    for i in zero_days:
        df.ix[i,column]=1
    return df

def eliminate_nan(df, column):
    new_df = df[df[column].notnull()]
    return new_df

def julian_date(df, date_col, new_col_name):
    df[new_col_name] = df[date_col].apply(lambda date: date.to_julian_date())
    return df

def mean_days(df, start_col, end_col):
    mean = np.sum(df[end_col]-df[start_col])/float(len(df))
    return mean

def impute_vei(df, col):
    array = df.as_matrix([col])
    imp = Imputer(missing_values = 'NaN', strategy = 'most_frequent', axis = 0)
    new_array = imp.fit_transform(array)
    return new_array

def impute_erup_length(df, start_date_col, end_date_col):
	