grade = input("Enter the Grade: ")
salary = float(input("Enter the Salary: "))
if grade == 'A':
    bonus = 0.05 * salary
elif grade == 'B':
    bonus = 0.1 * salary
else:
    print("Invalid Grade")
if salary < 10000:
    bonus += 0.02 * salary
total_salary = salary + bonus
print("Bonus",bonus)
print("Total salary",total_salary)
