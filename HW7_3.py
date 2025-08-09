def top_students(student_marks):
    highest = max(student_marks.values())
    
    toppers = []
    for name,marks in student_marks.items():
        if marks == highest:
            toppers.append(name)
            
    print("Highest Marks:", highest)
    print("Top Student(s):",toppers)

students = {
    "Alice": 88,
    "Bob": 92,
    "Charlie": 92,
    "David": 85
}

top_students(students)
