# Identidad y referencias

Utilice el operador `is` para comprobar si dos valores son exactamente el mismo objeto.

```python
>>> a = [1,2,3]
>>> b = a
>>> a is b
True
>>>
```

`is` compara la identidad del objeto (un entero). La identidad se puede obtener utilizando `id()`.

```python
>>> id(a)
3588944
>>> id(b)
3588944
>>>
```

Nota: Casi siempre es mejor utilizar `==` para comprobar objetos. El comportamiento de `is` a menudo es inesperado:

```python
>>> a = [1,2,3]
>>> b = a
>>> c = [1,2,3]
>>> a is b
True
>>> a is c
False
>>> a == c
True
>>>
```
