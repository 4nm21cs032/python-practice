'''
    Create a dictionary with at least students names as keys and their 
    respective grades as values
        - write the dictinoary file to grades.pkl using pickle module
        - read the dictinoary from the file and display the content
        - modify the grade of one student and save the updated
          dictionary back to the file
'''

import pickle
def create_stud_grade():
    n = int(input("no of students: "))
    my_dict = {} 
    for _ in range(n): 
        name = input("Enter name: ") 
        grade = input("Enter grade: ") 
        my_dict[name] = grade
    return my_dict

def save_grade_file(grades,filename):
    with open(filename,'wb') as file:
        pickle.dump(grades,file)
    print(f'Grades saved successfully in {filename}\n')

def read_grade(filename):
    with open(filename,'rb') as file:
        grades=pickle.load(file)
    print('Read from file')
    for student,grade in grades.items():
        print(f'Student name: {student}, Grade: {grade}')
    return grades

def modify_data(grades,student_name,new_grade,filename):
    if student_name in grades:
        grades[student_name]=new_grade
        save_grade_file(grades,filename)
        print(f'updated grade of {student_name} to {new_grade}')
    else:
        print(f'{student_name} not found')

if __name__=="__main__":
    filename='grades.pkl'
    stu_grades=create_stud_grade()

    save_grade_file(stu_grades,filename)

    grades=read_grade(filename)

    upd_name=input('Enter name whose grade is to be updates: ')
    new_grade=input('Enter new grade: ')
    modify_data(grades,upd_name,new_grade,filename)
    print('---After updating---')
    read_grade(filename)
