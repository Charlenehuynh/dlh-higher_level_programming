This file to keep track of explanation of code
Exercise 100: 
What are dunder methods?
They define how Python's built-in functions and operators behave on your objects. For example:
Dunder methodTriggered by__init__MyClass()__str__print() or str()__len__len()__add__+ operator

__str__ specifically
When you call print(sll), Python internally does:
pythonprint(sll.__str__())
So Python is asking your object — "how do you want to represent yourself as a string?"