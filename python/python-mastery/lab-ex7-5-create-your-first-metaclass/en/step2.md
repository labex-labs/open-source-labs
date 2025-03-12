# Creating Your First Metaclass

Now, we're going to create our very first metaclass. Before we start coding, let's understand what a metaclass is. In Python, a metaclass is a class that creates other classes. It's like a blueprint for classes. When you define a class in Python, Python uses a metaclass to create that class. By default, Python uses the `type` metaclass. In this step, we'll define a custom metaclass that prints information about the class it's creating. This will help us understand how metaclasses work under the hood.

1. Open VSCode in the WebIDE and create a new file called `mymeta.py` in the `/home/labex/project` directory. This is where we'll write our code for the metaclass.

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

Let's break down what this code does:

- First, we define a new class named `mytype` that inherits from `type`. Since `type` is the default metaclass in Python, by inheriting from it, we're creating our own custom metaclass.
- Next, we override the `__new__` method. In Python, the `__new__` method is a special method that's called when creating a new object. In the context of a metaclass, it's called when creating a new class.
- Inside our `__new__` method, we print some information about the class being created. We print the name of the class, its base classes, and its attributes. After that, we call the parent's `__new__` method using `super().__new__(meta, name, bases, __dict__)`. This is important because it actually creates the class.
- Finally, we create a base class named `myobject` and specify that it should use our custom metaclass `mytype`.

The `__new__` method takes the following parameters:

- `meta`: This refers to the metaclass itself. In our case, it's `mytype`.
- `name`: This is the name of the class that's being created.
- `bases`: This is a tuple containing the base classes that the new class inherits from.
- `__dict__`: This is a dictionary that contains the attributes of the class.

3. Save the file by pressing Ctrl+S or by clicking File > Save. Saving the file ensures that your code is preserved and can be run later.
