class Employee:
    company="ITC"
    def show(self):
        print(f"the name of the Employee is{self.name}and the salary is{self.salary}")

class programmer(Employee):
    company="INFOTECH"
    def showLanguage(self):
        print(f"the name is {self.name}and he is good with{self.language}language")

a=Employee()
b=programmer()

print(a.company,b.company)