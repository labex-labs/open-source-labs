# Static Methods

`@staticmethod` is used to define a so-called _static_ class methods (from C++/Java). A static method is a function that is part of the class, but which does _not_ operate on instances.

```python
class Foo(object):
    @staticmethod
    def bar(x):
        print('x =', x)

>>> Foo.bar(2) # x=2
>>>
```

Static methods are sometimes used to implement internal supporting code for a class. For example, code to help manage created instances (memory management, system resources, persistence, locking, etc). They're also used by certain design patterns (not discussed here).
