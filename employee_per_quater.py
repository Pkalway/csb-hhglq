import pandas as pd
import numpy as np

def employee_quater(df):

    df['EmpName'] = df['First Name'] + ' ' + df['Last Name']

    df1 = df.sort_values(['Date of Birth']).groupby('Quarter of Joining')['EmpName'].agg(list)  

    print(df1)
#    print(df)

if __name__ == '__main__':

    df = pd.read_csv('Data\employee.csv', parse_dates=['Date of Birth', 'Date of Joining'])
    employee_quater(df)
