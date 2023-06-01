from lib.employee import *
from lib.manager import *

# Test your code here

# e.g.
#   m1 = Manager( 'Mr. Levi', 'HR', 33 )
#   e1 = Employee( 'Norris', 40000, m1 )

# Managers

m1 = Manager("Janet", "Product Support", 23)
m2 = Manager("Edna", "Engineering", 26)
m3 = Manager("Amanda", "Marketing", 33)

# Employees

e1 = Employee("Carlisle", 100000, m1)
e2 = Employee("Belinda", 101000, m1)
e3 = Employee("Lynel", 99900, m2)
e4 = Employee("Dust mite", 1, m2)


# do not remove
import ipdb; ipdb.set_trace()
