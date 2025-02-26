# Usando getattr()

La función `getattr()` es extremadamente útil para escribir código que procesa objetos de manera muy genérica. Para ilustrar, considere este ejemplo que imprime un conjunto de atributos definidos por el usuario:

```python
>>> s= Stock('GOOG', 100, 490.1)
>>> fields = ['name','shares','price']
>>> for name in fields:
           print(name, getattr(s, name))

name GOOG
shares 100
price 490.1
>>>
```
