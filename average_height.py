student_heights = input("enter student heights divided by 'space' ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
  total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(number_of_students)

average_height = round(total_height/number_of_students)

print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")