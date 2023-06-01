class Manager:

    all = []
    
    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age
        type(self).all.append(self)

    # Properties 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else: 
            raise AttributeError("Name must be a string")

    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self, department):
        if isinstance(department, str):
            self._department = department
        else: 
            raise AttributeError("Department must be a string")
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self._age = age
        else: 
            raise AttributeError("Age must be an integer")
        
    # Instance methods
    def employees(self):
        return [employee for employee in Employee.all 
                if employee.manager is self] 

    def hire_employee(self, employee_name, employee_salary):
        if (isinstance(employee_name, str)
            and isinstance(employee_salary, int)):
            Employee(employee_name, employee_salary, self)
            return f"{self.name} now managing {employee_name}"
        else: 
            raise Exception("Name must be a string; salary must be an integer")

    # Class methods 
    @classmethod
    def all_departments(cls):
        return [manager.department for manager in cls.all]

    @classmethod
    def average_age(cls):
        all_ages = [manager.age for manager in cls.all]
        if all_ages: return round((sum(all_ages) / len(all_ages)), 2)

from lib.employee import Employee