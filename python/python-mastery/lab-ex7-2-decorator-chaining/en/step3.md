# Applying Decorators to Class Methods

Now, we're going to explore how decorators interact with class methods. This can be a bit tricky because Python has different types of methods: instance methods, class methods, static methods, and properties. Decorators are functions that take another function and extend the behavior of the latter function without explicitly modifying it. When applying decorators to class methods, we need to pay attention to how they work with these different method types.

## Understanding the Challenge

Let's see what happens when we apply our `@logged` decorator to different types of methods. The `@logged` decorator is likely used to log information about the method calls.

1. Create a new file `methods.py` in the WebIDE. This file will contain our class with different types of methods decorated with the `@logged` decorator.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @logged
    @classmethod
    def class_method(cls):
        print("Class method called")
        return "class result"

    @logged
    @staticmethod
    def static_method():
        print("Static method called")
        return "static result"

    @logged
    @property
    def property_method(self):
        print("Property method called")
        return "property result"
```

In this code, we have a class `Spam` with four different types of methods. Each method is decorated with the `@logged` decorator, and some are also decorated with other built - in decorators like `@classmethod`, `@staticmethod`, and `@property`.

2. Let's test how it works. We'll run a Python command in the terminal to call these methods and see the output.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

When you run this command, you may notice some issues:

- The `@property` decorator might not work correctly with our `@logged` decorator. The `@property` decorator is used to define a method as a property, and it has a specific way of working. When combined with the `@logged` decorator, there could be conflicts.
- The order of decorators matters for `@classmethod` and `@staticmethod`. The order in which decorators are applied can change the behavior of the method.

## The Order of Decorators

When you apply multiple decorators, they are applied from bottom to top. This means that the decorator closest to the method definition is applied first, and then the ones above it are applied in sequence. For example:

```python
@decorator1
@decorator2
def func():
    pass
```

This is equivalent to:

```python
func = decorator1(decorator2(func))
```

In this example, `decorator2` is applied to `func` first, and then `decorator1` is applied to the result of `decorator2(func)`.

## Fixing the Decorator Order

Let's update our `methods.py` file to fix the decorator order. By changing the order of the decorators, we can make sure that each method works as expected.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @classmethod
    @logged
    def class_method(cls):
        print("Class method called")
        return "class result"

    @staticmethod
    @logged
    def static_method():
        print("Static method called")
        return "static result"

    @property
    @logged
    def property_method(self):
        print("Property method called")
        return "property result"
```

In this updated version:

- For `instance_method`, the order doesn't matter. Instance methods are called on an instance of the class, and the `@logged` decorator can be applied in any order without affecting its basic functionality.
- For `class_method`, we apply `@classmethod` after `@logged`. The `@classmethod` decorator changes the way the method is called, and applying it after `@logged` ensures that the logging works correctly.
- For `static_method`, we apply `@staticmethod` after `@logged`. Similar to the `@classmethod`, the `@staticmethod` decorator has its own behavior, and the order with the `@logged` decorator needs to be correct.
- For `property_method`, we apply `@property` after `@logged`. This ensures that the property behavior is maintained while also getting the logging functionality.

3. Let's test the updated code. We'll run the same command as before to see if the issues are fixed.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

You should now see proper logging for all method types:

```
Calling instance_method
Instance method called
instance result
Calling class_method
Class method called
class result
Calling static_method
Static method called
static result
Calling property_method
Property method called
property result
```

## Best Practices for Method Decorators

When working with method decorators, follow these best practices:

1. Apply method - transforming decorators (`@classmethod`, `@staticmethod`, `@property`) **after** your custom decorators. This ensures that the custom decorators can perform their logging or other operations first, and then the built - in decorators can transform the method as intended.
2. Be aware that the decorator execution happens at class definition time, not at method call time. This means that any setup or initialization code in the decorator will run when the class is defined, not when the method is called.
3. For more complex cases, you might need to create specialized decorators for different method types. Different method types have different behaviors, and a one - size - fits - all decorator may not work in all situations.
