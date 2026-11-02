class Employee:
    language="python"  # This is a class attribute
    Salary=1200000


harry=Employee()
harry.name="Harry"  # This is an instant attribute
print(harry.name,harry.language,harry.Salary)


rohan=Employee()
rohan.name="Rohan Roro Robinson"
print(rohan.name,rohan.Salary,rohan.language)

# Here name is object attribute and salary and language are attribute as they directly
# belong to the class 