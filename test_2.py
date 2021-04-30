

"""
start

create a list to show all 24 numbers (float)
capture user's input 24 times for their grades.
each time we capture the user's inout, we append the number to the list
sort the list ascending, then splice the items starting at index 2
once we have the percentage of grades that are above the average grade in the list,
we sum them up and divide by the amount numbers of percentage of grades that are above the average grade
output a message to the user

end
"""

"""
create list
capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

sort the list, then splice out the grades that have a percentage of grades that are below the average grade.

print message to user

"""

grades = []

grade = input("Enter the 1st grade: ")
grades.append(float(grade))

grade = input("Enter the 2nd grade: ")
grades.append(float(grade))

grade = input("Enter the 3rd grade: ")
grades.append(float(grade))

grade = input("Enter the 4th grade: ")
grades.append(float(grade))

grade = input("Enter the 5th grade: ")
grades.append(float(grade))

grade = input("Enter the 6th grade: ")
grades.append(float(grade))

grade = input("Enter the 7th grade: ")
grades.append(float(grade))

grade = input("Enter the 8th grade: ")
grades.append(float(grade))

grade = input("Enter the 9th grade: ")
grades.append(float(grade))

grade = input("Enter the 10th grade: ")
grades.append(float(grade))

grade = input("Enter the 11th grade: ")
grades.append(float(grade))

grade = input("Enter the 12th grade: ")
grades.append(float(grade))

grade = input("Enter the 13th grade: ")
grades.append(float(grade))

grade = input("Enter the 14th grade: ")
grades.append(float(grade))

grade = input("Enter the 15th grade: ")
grades.append(float(grade))

grade = input("Enter the 16th grade: ")
grades.append(float(grade))

grade = input("Enter the 17th grade: ")
grades.append(float(grade))

grade = input("Enter the 18th grade: ")
grades.append(float(grade))

grade = input("Enter the 19th grade: ")
grades.append(float(grade))

grade = input("Enter the 20th grade: ")
grades.append(float(grade))

grade = input("Enter the 21st grade: ")
grades.append(float(grade))

grade = input("Enter the 22nd grade: ")
grades.append(float(grade))

grade = input("Enter the 23rd grade: ")
grades.append(float(grade))

grade = input("Enter the 24th grade: ")
grades.append(float(grade))

grades.sort()

grades = grades[11:]

grades = sum(grades)

results = grades / 12

print("Average Grade {0:.11f}%".format(result))


