class Employee:
    language="python"
    salary=1200000

    def getinfo(self):
        print(f"the language is{self.language}.the salary is{self.salary}")

harry= Employee()
harry.language="Javascript"
# harry.getinfo()
Employee.getinfo(harry)