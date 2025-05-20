age = input("how old are you?")
# print (type(age))
max_age = 90
# print (type(max_age))

age_diff = max_age- int(age)

days_left = age_diff * 365
weeks_left = age_diff * 52
month_lef = age_diff * 12

message = f"you have {days_left} days, {weeks_left} weeks and {month_lef} month left"
print(message)
