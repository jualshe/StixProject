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
  score = student_scores[name]
  if score < 70:
    student_grades[name] = "Fail"
  elif 71 <= score < 80 :
    student_grades[name]= "Acceptable"
  elif 81 <= score < 90:
    student_grades[name] = "Exceeds Expectations"
  else:
    student_grades[name] = "Outstanding"



print(student_grades)

# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"