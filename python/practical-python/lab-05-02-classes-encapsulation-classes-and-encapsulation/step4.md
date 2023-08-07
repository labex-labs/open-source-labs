# Private Attributes

Any attribute name with leading `_` is considered to be _private_.

```python
class Person(object):
    def __init__(self, name):
        self._name = 0
```

As mentioned earlier, this is only a programming style. You can still access and change it.

```python
>>> p = Person('Guido')
>>> p._name
'Guido'
>>> p._name = 'Dave'
>>>
```

As a general rule, any name with a leading `_` is considered internal implementation whether it's a variable, a function, or a module name. If you find yourself using such names directly, you're probably doing something wrong. Look for higher level functionality.
