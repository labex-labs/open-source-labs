# Applying Decorators to Class Methods

Now let's explore how decorators interact with class methods. This can be tricky because there are different types of methods in Python: instance methods, class methods, static methods, and properties.

## Understanding the Challenge

Let's see what happens when we apply our `@logged` decorator to different types of methods:

1. Create a new file `methods.py` in the WebIDE:

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

2. Let's test how it works:

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

You may notice some issues:

- The `@property` decorator might not work correctly with our `@logged` decorator
- The order of decorators matters for `@classmethod` and `@staticmethod`

## The Order of Decorators

When you apply multiple decorators, they are applied from bottom to top. For example:

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

## Fixing the Decorator Order

Let's update our `methods.py` file to fix the decorator order:

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

- For `instance_method`, the order doesn't matter
- For `class_method`, we apply `@classmethod` after `@logged`
- For `static_method`, we apply `@staticmethod` after `@logged`
- For `property_method`, we apply `@property` after `@logged`

3. Let's test the updated code:

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

1. Apply method-transforming decorators (`@classmethod`, `@staticmethod`, `@property`) **after** your custom decorators
2. Be aware that the decorator execution happens at class definition time, not at method call time
3. For more complex cases, you might need to create specialized decorators for different method types
