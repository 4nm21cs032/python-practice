'''
    Define a structutred array to store srudent data with the following details
        - name (string)
        - age (integer)
        - marks (float)

        find:
        - student with highest marks
        - the average marks
        
'''

import numpy as np

stu_info=np.dtype([('name','U10'),('age','int32'),('marks','float64')])
students=np.array([('John',20,78.9),('Alice',21,90.0),('Bob',19,87.5)],dtype=stu_info)

top_Student=students[np.argmax(students['marks'])]
print(top_Student)

avg_marks=np.mean(students['marks'])
print(avg_marks)

print(students['name'])