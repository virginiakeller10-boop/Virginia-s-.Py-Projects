# Dictionary of students and their grades
student_grades = {
    "Angelique": [85,90,78],
    "Eldan": [92,88,95],
    "Luna" : [75,80,82],
}

# Calculate the average grade for each student
for student, grades in student_grades.items():
    average_grade = sum(grades) / len(grades)
    print (f"{student}: {average_grade}")

# Define a function to determine the letter grade
def determine_letter_grade (grade):
    if grade >=90:
        return "A"
    elif grade >=80:
        return "B"
    elif grade >=70:
        return "C"
    elif grade >=60:
        return "D"
    else:
        return "F"
    
# Determine the letter grade for each student    
for student, grades in student_grades.items ():
    average_grade = sum(grades) / len(grades)
    letter_grade = determine_letter_grade (average_grade)
    print (f" {student}: {letter_grade}")

# Find the student with the highest average grade
highest_average_grade = 0
top_student = ""
for student, grades in student_grades.items () :
    average_grade = sum(grades) / len(grades)
    if average_grade > highest_average_grade:
        highest_average_grade = average_grade
        top_student = student
print (f"Top student: {top_student} with an average grade {highest_average_grade}")

# Calculate the overall class average
total_grades = 0
total_students = 0
for student, grades in student_grades.items ():
    total_grades += sum (grades)
    total_students += len (grades)
class_average = total_grades / total_students
print (f"Class average: {class_average}")