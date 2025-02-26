# Erstellen Sie Ihren eigenen Deskriptor

Definieren Sie die Deskriptor-Klasse gemäß den Notizen:

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

Versuchen Sie nun, eine einfache Klasse zu definieren, die diesen Deskriptor verwendet:

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

Bedenken Sie die Tatsache, dass Sie den Punkt-Operator für ein bestimmtes Attribut eingefangen haben.
