'''
    YAML : Yet Another Markup Language
        > human readable data serialization lang
        > config and data exchange
        > support for complex data structure
        > DevOPs(kubernate configuraton, github actions)

    key value pair:
        name:(space)john
        age: 30

        list:
        skills:
            -(space)c
            - c++
            - python

        nested data
        person:
            name: john
            age: 30
            address:
                city:mangaluru
                zip:4658
                main: 4th cross road

        inline lists and dictinoary
        colors:[read,green, blue]
        person{name:john, age: 30}

'''


# # yaml to dictionary
import yaml
# yaml_data="""
# name: john
# age: 30
# skills:
#     - python
#     - kubernet
# """

# data=yaml.safe_load(yaml_data)
# print(data)

''' writing to yaml '''
# data={
#     'name':'jack',
#     'age':50,
#     'skills':['python','C']
# }
# yaml_string=yaml.dump(data)
# print(yaml_string)

'''
    1.convert the following python dict to yaml format
    and save ot to file

    employeee={
        "id":101,
        "name":"siri",
        "dept":"HR",
        "projects":['p1','p2']
    }
'''
# employeee={
#         "id":101,
#         "name":"siri",
#         "dept":"HR",
#         "projects":['p1','p2']
# }
# with open('emp.yaml','w') as file:
#     yaml.dump(employeee,file)
# print('YAML file created')


'''
2. create a yaml file to represent a company org
    - the CEO is "Michal"
    -The company has two departments: "Engineering" and "sales"
    -Engineering has two employees: Alice , Bob
    -sales has one employee: Carol
'''
employee="""
Company:
    Department:
        Engineering:
        Employee:
            - Alice
            - Bob
        Sales:
            - Carol
            - John
            - Jack
"""
# -----------------------------------------------
'''
    3. Write a python script to validate a Yaml file for syntex errors
# '''
# def validate_yaml(file_name):
#     try:
#         with open(file_name,'r') as file:
#             yaml.safe_load(file)
#         print('YAML file is valid one')
#     except yaml.YAMLError as e:
#         print(f'Error in yaml file {e}')
# validate_yaml('emp.yaml')

