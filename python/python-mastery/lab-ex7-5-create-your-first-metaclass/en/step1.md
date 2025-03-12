# Understanding Metaclasses

Metaclasses are an advanced but powerful feature in Python. As a beginner, you might be wondering what metaclasses are and why they're important. Before we start creating our first metaclass, let's take a moment to understand these concepts.

## What is a Metaclass?

In Python, everything is an object, and that includes classes. Just as a regular class is used to create instances, a metaclass is used to create classes. By default, Python uses the built - in `type` metaclass to create all classes.

Let's break down the class creation process step by step:

1. First, Python reads the class definition you've written in your code. This is where you define the name of the class, its attributes, and methods.
2. Then, Python collects important information about the class, such as the class name, any base classes it inherits from, and all of its attributes.
3. After that, Python passes this collected information to the metaclass. The metaclass is responsible for taking this information and creating the actual class object.
4. Finally, the metaclass creates and returns the new class.

A metaclass gives you the power to customize this class creation process. You can modify or inspect classes as they are being created, which can be very useful in certain scenarios.

Let's visualize this relationship to make it easier to understand:

```
Metaclass → creates → Class → creates → Instance
```

In this lab, we'll create our own metaclass. By doing so, you'll be able to see this class creation process in action and gain a better understanding of how metaclasses work.
