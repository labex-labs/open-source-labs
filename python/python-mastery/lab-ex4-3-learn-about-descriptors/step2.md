# Make your own descriptor

Define the descriptor class from the notes:

```python
# descrip.py

class Descriptor:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        print('%s:__get__' % self.name)
    def __set__(self, instance, value):
        print('%s:__set__ %s' % (self.name, value))
    def __delete__(self, instance):
        print('%s:__delete__' % self.name)
```

Now, try defining a simple class that uses this descriptor:

```python
>>> class Foo:
        a = Descriptor('a')
        b = Descriptor('b')
        c = Descriptor('c')

>>> f = Foo()
>>> f
<__main__.Foo object at 0x38e130> <class __main__.Foo>
>>> f.a
a:__get__
>>> f.b
b:__get__
>>> f.a = 23
a:__set__ 23
>>> del f.a
a:__delete__
>>>
```

Ponder the fact that you have captured the dot-operator for a
specific attribute.
