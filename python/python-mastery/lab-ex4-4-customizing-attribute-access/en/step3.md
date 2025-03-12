# Delegation as an Alternative to Inheritance

In object-oriented programming, reusing and extending code is a common task. There are two main ways to achieve this: inheritance and delegation.

**Inheritance** is a mechanism where a subclass inherits methods and attributes from a parent class. The subclass can choose to override some of these inherited methods to provide its own implementation.

**Delegation**, on the other hand, involves an object containing another object and forwarding specific method calls to it.

In this step, we will explore delegation as an alternative to inheritance. We'll implement a class that delegates some of its behavior to another object.

## Setting Up a Delegation Example

First, we need to set up the base class that our delegating class will interact with.

1. Create a new file called `base_class.py` in the `/home/labex/project` directory. This file will define a class named `Spam` with three methods: `method_a`, `method_b`, and `method_c`. Each method prints a message and returns a result. Here is the code to put in `base_class.py`:

```python
class Spam:
    def method_a(self):
        print('Spam.method_a executed')
        return "Result from Spam.method_a"

    def method_b(self):
        print('Spam.method_b executed')
        return "Result from Spam.method_b"

    def method_c(self):
        print('Spam.method_c executed')
        return "Result from Spam.method_c"
```

Next, we'll create the delegating class.

2. Create a new file called `delegator.py`. In this file, we'll define a class named `DelegatingSpam` that delegates some of its behavior to an instance of the `Spam` class.

```python
from base_class import Spam

class DelegatingSpam:
    def __init__(self):
        # Create an instance of Spam that we'll delegate to
        self._spam = Spam()

    def method_a(self):
        # Override method_a but also call the original
        print('DelegatingSpam.method_a executed')
        result = self._spam.method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('DelegatingSpam.method_c executed')
        return "Result from DelegatingSpam.method_c"

    def __getattr__(self, name):
        # For any other attribute/method, delegate to self._spam
        print(f"Delegating {name} to the wrapped Spam object")
        return getattr(self._spam, name)
```

In the `__init__` method, we create an instance of the `Spam` class. The `method_a` method overrides the original method but also calls the `Spam` class's `method_a`. The `method_c` method completely overrides the original method. The `__getattr__` method is a special method in Python that is called when an attribute or method that doesn't exist in the `DelegatingSpam` class is accessed. It then delegates the call to the `Spam` instance.

Now, let's create a test file to verify our implementation.

3. Create a test file named `test_delegation.py`. This file will create an instance of the `DelegatingSpam` class and call its methods.

```python
from delegator import DelegatingSpam

# Create a delegating object
spam = DelegatingSpam()

print("Calling method_a (overridden with delegation):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (not defined in DelegatingSpam, delegated):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

Finally, we'll run the test script.

4. Run the test script using the following commands in the terminal:

```bash
cd /home/labex/project
python3 test_delegation.py
```

You should see output similar to the following:

```
Calling method_a (overridden with delegation):
DelegatingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (not defined in DelegatingSpam, delegated):
Delegating method_b to the wrapped Spam object
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
DelegatingSpam.method_c executed
Result: Result from DelegatingSpam.method_c

Calling non-existent method_d:
Delegating method_d to the wrapped Spam object
Error: 'Spam' object has no attribute 'method_d'
```

## Delegation vs. Inheritance

Now, let's compare delegation with traditional inheritance.

1. Create a file called `inheritance_example.py`. In this file, we'll define a class named `InheritingSpam` that inherits from the `Spam` class.

```python
from base_class import Spam

class InheritingSpam(Spam):
    def method_a(self):
        # Override method_a but also call the parent method
        print('InheritingSpam.method_a executed')
        result = super().method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('InheritingSpam.method_c executed')
        return "Result from InheritingSpam.method_c"
```

The `InheritingSpam` class overrides the `method_a` and `method_c` methods. In the `method_a` method, we use `super()` to call the parent class's `method_a`.

Next, we'll create a test file for the inheritance example.

2. Create a test file named `test_inheritance.py`. This file will create an instance of the `InheritingSpam` class and call its methods.

```python
from inheritance_example import InheritingSpam

# Create an inheriting object
spam = InheritingSpam()

print("Calling method_a (overridden with super call):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (inherited from parent):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

Finally, we'll run the inheritance test.

3. Run the inheritance test using the following commands in the terminal:

```bash
cd /home/labex/project
python3 test_inheritance.py
```

You should see output similar to the following:

```
Calling method_a (overridden with super call):
InheritingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (inherited from parent):
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
InheritingSpam.method_c executed
Result: Result from InheritingSpam.method_c

Calling non-existent method_d:
Error: 'InheritingSpam' object has no attribute 'method_d'
```

## Key Differences and Considerations

Let's look at the similarities and differences between delegation and inheritance.

1. **Method Override**: Both delegation and inheritance allow you to override methods, but the syntax is different.

   - In delegation, you define your own method and decide whether to call the wrapped object's method.
   - In inheritance, you define your own method and use `super()` to call the parent's method.

2. **Method Access**:

   - In delegation, undefined methods are forwarded via the `__getattr__` method.
   - In inheritance, undefined methods are inherited automatically.

3. **Type Relationships**:

   - With delegation, `isinstance(delegating_spam, Spam)` returns `False` because the `DelegatingSpam` object is not an instance of the `Spam` class.
   - With inheritance, `isinstance(inheriting_spam, Spam)` returns `True` because the `InheritingSpam` class inherits from the `Spam` class.

4. **Limitations**: Delegation through `__getattr__` doesn't work with special methods like `__getitem__`, `__len__`, etc. These methods would need to be explicitly defined in the delegating class.

Delegation is particularly useful in the following situations:

- You want to customize an object's behavior without affecting its hierarchy.
- You want to combine behaviors from multiple objects that don't share a common parent.
- You need more flexibility than inheritance provides.

Inheritance is generally preferred when:

- The "is-a" relationship is clear (e.g., a Car is a Vehicle).
- You need to maintain type compatibility across your code.
- Special methods need to be inherited.
