'''
    Create 2 dataframes
    Products:productID, Category
    Sales:SalesID, ProductID, unit_sold, Revenue

    perform:
    -Merge the 2 dataframes to create a combined view of sale data
    -Calcuate the total revenue for each product category
    -Reshape the data to show products as rows and metrics(units sold, revenue) as columns 
'''
import pandas as pd
products=pd.DataFrame({
    'productId':[1,2,3],
    'Name':['Mobile','cloth','Oven'],
    'Category':['Electronics','Textile','Electronics']
})

sales=pd.DataFrame({
    'salesId':[101,102,103,104],
    'productId':[1,2,3,1],
    'Units-sold':[10,12,29,10],
    'Revenue':[1100,2500,3000,1000]
})

# merging DFs
merge_df=pd.merge(sales,products,on='productId',how='inner')
# total rev
total_rev=merge_df.groupby('Category')['Revenue'].sum()

reshape_df=merge_df.pivot_table(
    values=['Units-sold','Revenue'],
    index='Name',
    aggfunc=sum
)

print(f'Merged DF:\n{merge_df}\n--------------\n')
print(f'Total Rev:\n{total_rev}\n--------------\n')
print(f'Redhape DF:\n{reshape_df}\n--------------\n')
