student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {
}

# TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
  if student_scores[name] < 70:
    student_grades[name] = "Fail"
  if 71 <= student_scores[name] < 80 :
    student_grades[name]= "Acceptable"
  if 81 <= student_scores[name] < 90:
    student_grades[name] = "Exceeds Expectations"
  if 91 <= student_scores[name] < 100:
    student_grades[name] = "Outstanding"



print(student_grades)

# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"