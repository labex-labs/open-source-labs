# Cómo funciona la herencia

Las clases pueden heredar de otras clases.

```python
class A(B, C):
 ...
```

Las clases base se almacenan en una tupla en cada clase.

```python
>>> A.__bases__
(<class '__main__.B'>, <class '__main__.C'>)
>>>
```

Esto proporciona un enlace a las clases padre.
