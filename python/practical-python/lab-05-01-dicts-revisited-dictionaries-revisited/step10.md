# Reading Attributes with Inheritance

Logically, the process of finding an attribute is as follows. First, check in local `__dict__`. If not found, look in `__dict__` of the class. If not found in class, look in the base classes through `__bases__`. However, there are some subtle aspects of this discussed next.
