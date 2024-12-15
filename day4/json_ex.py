'''
    JSON:
        > lightweogth data interchnage format
        > human read write for machines
        > parsing very easy
        > mainly used for transmitting data btw server and client
        > 
'''
import json
# json_data='{"name":"john", "age": 20, "city":"Udupi"}'
# #convert Json string to python dictionary
# data=json.loads(json_data)
# print(data)
# print(json_data)

# print(data['name'])
# print(json_data['name'])    # not possible

''' Write to file '''
# data={"name":"Anil", "age":33, "city":"Myuru"}
# with open('data.json', 'w') as file:
#     json.dump(data, file)                           #**difference betwenn dump and dumps
# print("data written sucessfully")

''' Read form file '''
# with open('data.json','r')as file:
#     data=json.load(file)
# print(data)

'''-------------------------------------------'''

# json_data='{"name":"John","age":30,"skills":["python","C"]}'
# data=json.loads(json_data)
# print(data)

# #  dictionary to json
# data={'name': 'John', 'age': 30, 'city': 'Goa'}
# json_data=json.dumps(data)
# print(json_data)


# # pretty-printing
# data={'name': 'John', 'age': 30, 'city': 'Goa'}
# json_data=json.dumps(data,indent=4)
# print(json_data)