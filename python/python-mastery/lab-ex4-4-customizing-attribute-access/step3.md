# Delegation as an alternative to inheritance

Delegation is sometimes used as an alternative to inheritance. The idea is almost the same as the proxy class you defined in part (b). Try defining the following class:

```python
>>> class Spam:
        def a(self):
            print('Spam.a')
        def b(self):
            print('Spam.b')

>>>
```

Now, make a class that wraps around it and redefines some of the methods:

```python
>>> class MySpam:
        def __init__(self):
            self._spam = Spam()
        def a(self):
            print('MySpam.a')
            self._spam.a()
        def c(self):
            print('MySpam.c')
        def __getattr__(self, name):
            return getattr(self._spam, name)

>>> s = MySpam()
>>> s.a()
MySpam.a
Spam.a
>>> s.b()
Spam.b
>>> s.c()
MySpam.c
>>>
```

Carefully notice that the resulting class looks very similar to inheritance. For example the `a()` method is doing something similar to the `super()` call. The method `b()` is picked up via the `__getattr__()` method which delegates to the internally held `Spam` instance.

**Discussion**

The `__getattr__()` method is commonly defined on classes that act as wrappers around other objects. However, you have to be aware that the process of wrapping another object in this manner often introduces other complexities. For example, the wrapper object might break type-checking if any other part of the application is using the `isinstance()` function.

Delegating methods through `__getattr__()` also doesn't work with special methods such as `__getitem__()`, `__enter__()`, and so forth. If a class makes extensive use of such methods, you'll have to provide similar functions in your wrapper class.
