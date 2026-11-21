students = {
    101: {"name": "Ali", "age": 20, "course": "Python"},
    102: {"name": "Sara", "age": 21, "course": "Data Science"},
    103: {"name": "John", "age": 22, "course": "Machine Learning"}
}

def search_student(student_id):
    if student_id in students:
        print("Student Found:")
        print(students[student_id])
    else:
        print("Student Not Found")

def add_student(student_id, name, age, course):
    students[student_id] = {
        "name": name,
        "age": age,
        "course": course
    }
    print("Student Added Successfully")

def update_student(student_id, name, age, course):
    if student_id in students:
        students[student_id] = {
            "name": name,
            "age": age,
            "course": course
        }
        print("Student Updated Successfully")
    else:
        print("Student Not Found")

print("=== Search Operation ===")
search_student(101)

print("\n=== Add Operation ===")
add_student(104, "David", 23, "AI")

print("\n=== Update Operation ===")
update_student(101, "Ali Khan", 20, "Artificial Intelligence")

print("\n=== Final Student Records ===")
for sid, info in students.items():
    print(sid, info)
