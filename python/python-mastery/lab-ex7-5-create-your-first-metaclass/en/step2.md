# Creating Your First Metaclass

Now let's create our first metaclass. In this step, we'll define a metaclass that prints information about the class it's creating.

1. Open VSCode in the WebIDE and create a new file called `mymeta.py` in the `/home/labex/project` directory.

2. Add the following code to the file:

```python
# mymeta.py

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__)

class myobject(metaclass=mytype):
    pass
```

Let's understand what this code does:

- We define a new class `mytype` that inherits from `type` (the default metaclass)
- We override the `__new__` method, which is called when creating a new class
- Our `__new__` method prints information about the class being created, then calls the parent's `__new__` method
- We create a base class `myobject` that uses our metaclass

The `__new__` method parameters are:

- `meta`: The metaclass itself
- `name`: The name of the class being created
- `bases`: The base classes the new class inherits from
- `__dict__`: A dictionary containing the attributes of the class

3. Save the file by pressing Ctrl+S or by clicking File > Save.
