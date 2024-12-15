def read_students_data(filename='student.txt'):
    student={}
    with open(filename, 'r') as file:
        for i in file:
            name, grade=i.strip().split(',')
            student[name]= grade
    return student

def cal_avg_grade(grades):
    grade_map={"A":4, "B":3, "C":2, "D":1, "F":0}
    numeric_grade=[grade_map[grade] for grade in grades]
    avg=sum(numeric_grade)/len(numeric_grade)
    # reverse_mapping={v:k for k,v in grade_map in grades}
    round_avg=round(avg)
    return avg, round_avg

def low_high_grade(students):
    sort_stud= sorted(students.items(), key=lambda x: x[1], reverse=True)
    highest_students, highest_grade=sort_stud[0]
    low_student, lowest_grade=sort_stud[-1]
    return (highest_students,highest_grade), (low_student, lowest_grade)

if __name__=="__main__":
    students=read_students_data()
    avg, avg_grade=cal_avg_grade(students.values())
    print(f"average grade: {avg}")
    print(f"average grade: {avg_grade}")
    highest, lowest=low_high_grade(students)