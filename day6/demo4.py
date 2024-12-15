import matplotlib.pyplot as plt
import pandas as pd

''' Line plot '''
# x=[1,2,3,4,5]
# y=[2,4,1,6,3]
# plt.plot(x,y, label='sample line graph', color='blue',linestyle=':')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('line plot example')
# plt.show()

''' Scatter plot '''
# x=[1,2,3,4,5]
# y=[2,1,6,8,10]
# plt.scatter(x,y,color='blue')
# plt.title('Scatter plot example')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

''' Bar graph '''
# category=['A','B','C','D']
# value=[3,5,9,2]
# plt.bar(category,value, color='lightgreen')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

''' Pie Chart '''
# category=['A','B','C','D']
# value=[30,54,10,80]
# plt.pie(value,labels=category)
# plt.show()

''' Dataframe plotting '''
# data={
#     'x':[1,2,3,4],
#     'y':[10,20,15,40]
# }
# df=pd.DataFrame(data)
# df.plot(x='x',y='y',kind='bar')
# plt.show()

''' subplots '''
x=[1,2,3,4,5]
plt.subplot(3,1,1)
plt.plot(x,[2,4,5,8,10],'r')
plt.grid(True)
plt.title('First plot')

plt.subplot(3,1,2)
plt.scatter(x,[1,6,7,4,5],color='blue')
plt.grid(True)
plt.title('Second Plot')

plt.subplot(3,1,3)
plt.pie([11,16,27,14,25],labels=x)
plt.title('Third Plot')

plt.tight_layout()
plt.show()