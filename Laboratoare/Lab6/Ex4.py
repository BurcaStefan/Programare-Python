class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def display(self):
        super().display()
        print("Bonus: ", self.bonus)
        
    def hire_employee(self, employee):
        print(f"{self.name} a angajat pe {employee.name}.")
        
    def manage_employee(self, employee):
        print(f"{self.name} il supravegheaza pe {employee.name}.")
        
class Engineer(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def display(self):
        super().display()
        print("Bonus: ", self.bonus)
        
    def develop_software(self, software):
        print(f"{self.name} a dezvoltat {software}.")
        
class Salesman(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
        
    def sale_product(self, product):
        print(f"{self.name} a vandut {product}.")
        
        
manager = Manager("Ion", 1000, 200)
manager.display()
manager.hire_employee(Employee("Mihai", 500))
manager.manage_employee(Employee("Mihai", 500))

engineer = Engineer("Mihai", 500, 100)
engineer.display()
engineer.develop_software("Python")

salesman = Salesman("Vasile", 700, 150)
salesman.display()
salesman.sale_product("Proiectul la Python")