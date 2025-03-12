# Understanding Metaclasses

Metaclasses are an advanced but powerful feature in Python. Before creating our first metaclass, let's understand what they are and why they're useful.

## What is a Metaclass?

In Python, classes are objects too. Just like how a regular class creates instances, a metaclass creates classes. By default, Python uses the built-in `type` metaclass to create all classes.

The class creation process follows these steps:

1. Python reads the class definition
2. Python collects the class name, base classes, and attributes
3. Python passes this information to the metaclass
4. The metaclass creates and returns the new class

A metaclass allows you to customize this class creation process, giving you the ability to modify or inspect classes as they are being created.

Let's visualize this relationship:

```
Metaclass → creates → Class → creates → Instance
```

In this lab, we'll create our own metaclass to observe this process in action.
