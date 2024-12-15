'''
    Create 2 DFs
        - Customers : custId,name
        - Orders : orderId,custid,product,amt
    
        > perfrm inner join to find all order with cust-name
        > find total amt spent by each cust
'''

import pandas as pd
# customer=pd.DataFrame({
#     'CustId':[1,2,3],
#     'Name':['John','Jack','Jill']
# })
# orders=pd.DataFrame({
#     'OrderId':[101,102,103,104,105],
#     'CustId':[1,1,3,2,3],
#     'Product':['p1','p2','p3','p4','p5'],
#     'Amount':[300,400,500,400,300]
# })

# # inner join
# inner_join=pd.merge(orders,customer,on='CustId',how='inner')
# total_spent=inner_join.groupby('Name')['Amount'].sum()
# print(f'Joined DF:\n{inner_join}\n------------\ntotalspent:\n{total_spent}')

'''
    create DF with following emp data
        > name
        > Dept
        > salary
        > Joining date
        > performance score
    
        perform following
        - filter employees with performance score
        - find emp with longest tenure in the company
        - grp emps by dept and calc avg salary in each dept
'''

data={
    'Name':['Siri','Giri','Hari','Santa','Sujan'],
    'Department':['HR','IT','Sales','HR','IT'],
    'Salary':[30000,40000,450000,560000,980000],
    "Joining-date":pd.to_datetime([
        '2024-01-15','2024-05-10','2021-05-20','2019-11-29','2013-01-01'
    ]),
    'Performance-Score':[88,77,98,99,70]
}
df=pd.DataFrame(data)
avg_performance=df.groupby('Department')['Performance-Score'].transform('mean')

above_avg_perf=df[df['Performance-Score']>avg_performance]
print(f'Filtered Performance:\n{above_avg_perf}\n-----------------\n')

# find emp woth long tenuire
tenure=((pd.Timestamp.now())-df['Joining-date']).dt.days
long_tenure=df.loc[tenure.idxmax()]
print(f'Long tenure :\n{long_tenure}\n-----------------\n')

avg_sal_dept=df.groupby('Department')['Salary'].mean()
print(f'Avg salary of eacch Dept :\n{avg_sal_dept}\n-----------------\n')
