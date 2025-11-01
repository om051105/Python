# Function to check how many students are absent in all subjects
def absent_students(data):
    count = 0
    for student in data:
        if student['math'] == 'A' and student['science'] == 'A' and student['english'] == 'A':  # A = Absent
            count = count + 1
    return count

# main part
students = [
    {'name': 'Riya', 'math': 'a', 'science': 'A', 'english': 'A'},
    {'name': 'Amit', 'math': 'a', 'science': 'A', 'english': 'A'},
    {'name': 'Tina', 'math': 'A', 'science': 'P', 'english': 'A'},
    {'name': 'Rahul', 'math': 'a', 'science': 'A', 'english': 'A'}
]

# i think this will give total absent students
result = absent_students(students)
print("total absent student in all subject is :", result)

