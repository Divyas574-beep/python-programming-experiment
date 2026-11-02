name = input("Enter your name: ")
n = int(input("Enter the number of subjects: "))
if n <= 0:
    raise ValueError("The number of subjects must be greater than zero.")

total = 0
for i in range(1, n + 1):
    mark = float(input(f"Enter your mark for subject {i}: "))
    total += mark

percentage = total / n
if percentage >= 90:
    Grade = "A+"
    performance = "outstanding"
elif percentage >= 80:
    Grade = "A"
    performance = "Excellent"
elif percentage >= 70:
    Grade = "B"
    performance = "very good"
elif percentage >= 60:
    Grade = "C"
    performance = "good"
elif percentage >= 50:
    Grade = "D"
    performance = "Average"
else:
    Grade = "F"
    performance = "Needs improvement"

print("------Academic performance------")
print("Student Name:", name)
print("Total marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", Grade)
print("Performance:", performance)