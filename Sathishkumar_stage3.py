# Input
name = input("Enter student name: ")
m1 = float(input("Enter marks for Subject 1 (0-100): "))
m2 = float(input("Enter marks for Subject 2 (0-100): "))
m3 = float(input("Enter marks for Subject 3 (0-100): "))

# Calculate total and percentage
total = m1 + m2 + m3
percentage = (total / 300) * 100

# Grade
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# Output
print("\n--- Output ---")
print(name)
print("Total:", int(total), "/300")
print("Percentage:", round(percentage, 1), "%")
print("Grade:", grade)