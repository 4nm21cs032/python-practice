# files and directory

# # ->  writ to file
# with open('in.txt','w') as file:
#     file.write('I am batman!!')
#     file.write('Welcome to Gotham')

#  -> read data from file
'''     >> read()
        >> readLine()
        >>readLines()        
'''
# with open('in.txt','r') as file:
#     content=file.read()
#     print(content)
'''
    .tell() will give you the cursor position 
    .seek() is used to change the cursor position
'''
# with open('in.txt','r') as file:
#     print(file.tell())
#     file.seek(1)
#     print(file.read())

#dictionary
# person={"name":'Anil',"age":30,"city":"udupi"}
# print(person['name'])
# person['job']='developer'
# print(person)
# person['name']='Tom'
# print(person)

'''
    # Pickle module
        -> serialize and deserialize python objs(include the dict)
'''
# import pickle
# data1={'name':'alice','age':15,'city':'Bangalore'}
# with open('data.pkl','wb') as file:
#     pickle.dump(data1,file)
# with open('data.pkl','rb') as file:
#     load=pickle.load(file)
#     print(load)

'''
    write a python pgm accepts a list of studrnts(name , grade)
    as a inp from user . saves data in text file whr each students name and grade 
    or on new line seperated by comma.
    after saving pgm shd res data from file and disp
'''
def get_stud_data():
    n=int(input("Enter number of students: "))
    l=[]
    for i in range(n):
        name=input('Enter name: ')
        grade=input('Enter grade: ')
        print('\n')
        l.append([name,grade])
    return l

def save_file(students,filename="student.txt"):
    with open(filename,'w') as file:
        for name,grade in students:
            file.write(f'{name} {grade},\n')
    print(f'saved successfully in {filename}\n')

def read_file(filename='student.txt'):
    with open(filename,'r') as file:
        for i in file:
            name,grade=i.strip().split()
            print(f'Name:{name}\tGrade:{grade}')


if __name__=="__main__":
    students=get_stud_data()
    save_file(students)
    read_file()
