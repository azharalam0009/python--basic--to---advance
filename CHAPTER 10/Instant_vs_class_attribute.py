class Employee:
    language="python"  # This is a class attribute
    Salary=1200000


harry=Employee()
harry.language="Javascript"  # This is an instant attribute
print(harry.language,harry.Salary)


# instance Attribute takes preference over class.  