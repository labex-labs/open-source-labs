# Creating Custom Descriptors

In this step, we're going to create our own descriptor class. But first, let's understand what a descriptor is. A descriptor is a Python object that implements the descriptor protocol, which consists of the `__get__`, `__set__`, and `__delete__` methods. These methods allow the descriptor to manage how an attribute is accessed, set, and deleted. By creating our own descriptor class, we can better understand how this protocol works.

Create a new file called `descrip.py` in the project directory. This file will contain our custom descriptor class. Here's the code:

```python
# descrip.py

class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print(f'{self.name}:__get__')
        # In a real descriptor, you would return a value here

    def __set__(self, instance, value):
        print(f'{self.name}:__set__ {value}')
        # In a real descriptor, you would store the value here

    def __delete__(self, instance):
        print(f'{self.name}:__delete__')
        # In a real descriptor, you would delete the value here
```

In the `Descriptor` class, the `__init__` method initializes the descriptor with a name. The `__get__` method is called when the attribute is accessed, the `__set__` method is called when the attribute is set, and the `__delete__` method is called when the attribute is deleted.

Now, let's create a test file to experiment with our custom descriptor. This will help us see how the descriptor behaves in different scenarios. Create a file named `test_descrip.py` with the following code:

```python
# test_descrip.py

from descrip import Descriptor

class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

# Create an instance and try accessing the attributes
if __name__ == '__main__':
    f = Foo()
    print("Accessing attribute f.a:")
    f.a

    print("\nAccessing attribute f.b:")
    f.b

    print("\nSetting attribute f.a = 23:")
    f.a = 23

    print("\nDeleting attribute f.a:")
    del f.a
```

In the `test_descrip.py` file, we import the `Descriptor` class from `descrip.py`. Then we create a class `Foo` with three attributes `a`, `b`, and `c`, each managed by a descriptor. We create an instance of `Foo` and perform operations like accessing, setting, and deleting attributes to see how the descriptor methods are called.

Now let's run this test file to see the descriptors in action. Open your terminal, navigate to the project directory, and run the test file using the following commands:

```bash
cd ~/project
python3 test_descrip.py
```

You should see output like this:

```
Accessing attribute f.a:
a:__get__

Accessing attribute f.b:
b:__get__

Setting attribute f.a = 23:
a:__set__ 23

Deleting attribute f.a:
a:__delete__
```

As you can see, each time you access, set, or delete an attribute that is managed by a descriptor, the corresponding magic method (`__get__`, `__set__`, or `__delete__`) is called.

Let's also examine our descriptor interactively. This will allow us to test the descriptor in real - time and see the results immediately. Open your terminal, navigate to the project directory, and start an interactive Python session with the `descrip.py` file:

```bash
cd ~/project
python3 -i descrip.py
```

Now type these commands in the interactive Python session to see how the descriptor protocol works:

```python
class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

f = Foo()
f.a         # Should call __get__
f.b         # Should call __get__
f.a = 23    # Should call __set__
del f.a     # Should call __delete__
exit()
```

The key insight here is that descriptors provide a way to intercept and customize attribute access. This makes them powerful for implementing data validation, computed attributes, and other advanced behaviors. By using descriptors, you can have more control over how your class attributes are accessed, set, and deleted.
