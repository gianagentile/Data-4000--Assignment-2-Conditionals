# Problem 2: Employee Performance Bonus
# prompts user for annual salary and performance score 
annual_salary = float(input("Enter the employee's annual salary: "))
performance_score = float(input("Enter the employee's performance score (1-100): "))

# bonus percentage 
bonus_percentage = 0

# determine bonus percentage based on performance score
if 90 <= performance_score <= 100:
    bonus_percentage = 20
elif 80 <= performance_score < 89:
    bonus_percentage = 10
elif 70 <= performance_score < 79:
    bonus_percentage = 5
elif 0 <= performance_score < 70:
    bonus_percentage = 0
else:
    print("Invalid performance score. Please enter a score between 0 and 100.")
    exit()

# calculate bonus amount
bonus_amount = (bonus_percentage / 100) * annual_salary

# print results 
print(f"Performance Bonus: {bonus_percentage}%")
print(f"Bonus Amount: ${bonus_amount:.2f}")