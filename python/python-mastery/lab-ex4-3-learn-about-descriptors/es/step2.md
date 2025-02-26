# Crea tu propio descriptor

Define la clase descriptor a partir de las notas:

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

Ahora, intenta definir una clase simple que utilice este descriptor:

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

Reflexiona sobre el hecho de que has capturado el operador de punto para un atributo específico.
