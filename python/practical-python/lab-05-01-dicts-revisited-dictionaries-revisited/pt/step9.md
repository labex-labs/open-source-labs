# Como a herança funciona

Classes podem herdar de outras classes.

```python
class A(B, C):
    ...
```

As classes base são armazenadas em uma tupla em cada classe.

```python
>>> A.__bases__
(<class '__main__.B'>, <class '__main__.C'>)
>>>
```

Isso fornece um link para as classes pai.
