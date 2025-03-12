# Creating Custom Descriptors

In this step, we'll create our own descriptor class to better understand how the descriptor protocol works.

Create a new file called `descrip.py` in the project directory:

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

Now create a test file to experiment with our custom descriptor:

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

Now let's run this test file to see the descriptors in action:

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

Each time you access, set, or delete an attribute that is managed by a descriptor, the corresponding magic method is called.

Let's also examine our descriptor interactively:

```bash
cd ~/project
python3 -i descrip.py
```

Now type these commands to see how the descriptor protocol works:

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

The key insight here is that descriptors provide a way to intercept and customize attribute access. This makes them powerful for implementing data validation, computed attributes, and other advanced behaviors.
