'''
    Create a multiindex DF witht he following data
        Sales Data:
            > Product: ['A','A','B','B','C','C']
            > Region: ['North','South','North','South','North','South']
            > Years: [2021,2021,2021,2022,2021,2022]
            > sales:[100,120,150,200,300,350]

    - Extract sales data for product 'B' in 'north' region
    - calc total sale for each region

'''
import pandas as pd
# data={
#     'Product': ['A','A','B','B','C','C'],
#     'Region': ['North','South','North','South','North','South'],
#     'Years': [2021,2021,2021,2022,2021,2022],
#     'Sales':[100,120,150,200,300,350]
# }

# df=pd.DataFrame(data).set_index(['Product','Region','Years'])

# north_reg_sales=df.loc[('B','North')]
# total_sal=df.groupby(level='Region')['Sales'].sum()

# print(f'North regrionSales:\n{north_reg_sales}\n-----------\nTotal sales:\n{total_sal}')



'''
    Create a series with the daily sales of the store from '2024-01-01'
    to '2024-01-10'
    perfrom the following:
        - calcuate the 3 day rolling avg sales
        - Filter the days where sales are above the eolling average

'''
import numpy as np
# dates=pd.date_range(start='2024-01-01',end='2024-01-10')
# sales=pd.Series([200,220,300,250,240,258,301,345,300,120],index=dates)
# roll_avg=sales.rolling(window=3).mean()         #  computes a rolling window of size 3 for the Series.
# # abv rolling avg
# above_avg=sales[sales>roll_avg]
# print(f'Roll Data:\n{roll_avg}\nAbove avg:\n{above_avg}')


'''
    Create Df rep customer purchase
        'Customer':['C1','C2','C3','C1','C2','C3']
        'Product':['P1','P1','P2','P2','P3','P1']
        'Amount':[400,500,700,400,800,200]
        'Date':['2024-01-01','2024-01-02','2024-01-03','2024-01-04','2024-01-05','2024-01-06']

    perform fiollowing:
        - calc total amt by each customer
        - find the customer who spent more
        - identify products purchased by 'C1'
'''
cust_data={
    'Customer':['C1','C2','C3','C1','C2','C3'],
    'Product':['P1','P1','P2','P2','P3','P1'],
    'Amount':[400,500,700,400,800,200],
    'Date':pd.to_datetime(['2024-01-01','2024-01-02','2024-01-03','2024-01-04','2024-01-05','2024-01-06'])
}

cust_df=pd.DataFrame(cust_data)
total_amt=cust_df.groupby('Customer')['Amount'].sum()
print(f'Total amt by each customer:\n{total_amt}\n--------------\n')

highest_purch=total_amt.idxmax()
print(f'customer with highest purchase:\n{highest_purch}\n--------------\n')

prod_c1=cust_df[cust_df['Customer']=='C1']['Product'].unique()
print(f'product purchased by C1:\n{prod_c1}')