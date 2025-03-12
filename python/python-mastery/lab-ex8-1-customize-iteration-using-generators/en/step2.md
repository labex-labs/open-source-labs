# Adding Iteration to Custom Classes

Now that you have grasped the basics of generators, we're going to use them to add iteration capabilities to custom classes. In Python, if you want to make a class iterable, you need to implement the `__iter__()` special method. An iterable class allows you to loop through its elements, just like you can loop through a list or a tuple. This is a powerful feature that makes your custom classes more flexible and easier to work with.

## Understanding the `__iter__()` Method

The `__iter__()` method is a crucial part of making a class iterable. It should return an iterator object. An iterator is an object that can be iterated (looped) over. A simple and effective way to achieve this is by defining `__iter__()` as a generator function. A generator function uses the `yield` keyword to produce a sequence of values one at a time. Each time the `yield` statement is encountered, the function pauses and returns the value. The next time the iterator is called, the function resumes from where it left off.

## Modifying the Structure Class

In the setup for this lab, we provided a base `Structure` class. Other classes, like `Stock`, can inherit from this `Structure` class. Inheritance is a way to create a new class that inherits the properties and methods of an existing class. By adding an `__iter__()` method to the `Structure` class, we can make all its subclasses iterable. This means that any class that inherits from `Structure` will automatically have the ability to be looped over.

1. Open the file `structure.py` in the WebIDE:

```bash
cd ~/project
```

This command changes the current working directory to the `project` directory where the `structure.py` file is located. You need to be in the correct directory to access and modify the file.

2. Look at the current implementation of the `Structure` class:

```python
class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)
```

The `Structure` class has a `_fields` list that stores the names of the attributes. The `__init__()` method is the constructor of the class. It initializes the object's attributes by checking if the number of arguments passed is equal to the number of fields. If not, it raises a `TypeError`. Otherwise, it sets the attributes using the `setattr()` function.

3. Add an `__iter__()` method that yields each attribute value in order:

```python
def __iter__(self):
    for name in self._fields:
        yield getattr(self, name)
```

This `__iter__()` method is a generator function. It loops through the `_fields` list and uses the `getattr()` function to get the value of each attribute. The `yield` keyword then returns the value one by one.

The complete `structure.py` file should now look like this:

```python
class StructureMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = clsdict.get('_fields', [])
        for name in fields:
            clsdict[name] = property(lambda self, name=name: getattr(self, '_'+name))
        return super().__new__(cls, name, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
```

This updated `Structure` class now has the `__iter__()` method, which makes it and its subclasses iterable.

4. Save the file.
   After making changes to the `structure.py` file, you need to save it so that the changes are applied.

5. Now let's test the iteration capability by creating a `Stock` instance and iterating over it:

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('Iterating over Stock:'); [print(val) for val in s]"
```

This command creates an instance of the `Stock` class, which inherits from the `Structure` class. It then iterates over the instance using a list comprehension and prints each value.

You should see output like this:

```
Iterating over Stock:
GOOG
100
490.1
```

Now any class that inherits from `Structure` will automatically be iterable, and iteration will yield the attribute values in the order defined by the `_fields` list. This means that you can easily loop through the attributes of any subclass of `Structure` without having to write additional code for iteration.
