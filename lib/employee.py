class Employee:

    all = []

    def __init__(self, name, salary, manager):
        self.name = name 
        self.salary = salary 
        self.manager = manager 
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
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary): 
        if isinstance(salary, int):
            self._salary = salary
        else: 
            raise AttributeError("Salary must be an integer")
    
    @property
    def manager(self):
        return self._manager
    
    @manager.setter
    def manager(self, manager): 
        if isinstance(manager, Manager):
            self._manager = manager
        else: 
            raise AttributeError("Manager must be an instance of Manager")

    # Instance methods
    def tax_bracket(self):
        return [employee for employee in type(self).all 
                if ((self.salary - 1000) <= employee.salary <= (self.salary + 1000))
                and employee is not self] 

    # Class methods
    @classmethod
    def paid_over(cls, amt):
        if isinstance(amt, int):
            return [employee for employee in cls.all if employee.salary > amt]
        else: 
            raise Exception("Amount paid must be an integer")

    @classmethod
    def find_by_department(cls, dept):
        if isinstance(dept, str):
            for employee in cls.all: 
                if employee.manager.department == dept: 
                    return employee  
            return "No employees in that department"
        else: 
            raise Exception("Department must be a string")


from lib.manager import Manager

