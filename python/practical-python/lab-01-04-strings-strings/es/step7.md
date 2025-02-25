# Inmutabilidad de cadenas

Las cadenas son "inmutables" o de solo lectura. Una vez creadas, no se puede cambiar su valor.

```python
>>> s = 'Hello World'
>>> s[1] = 'a'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError:'str' object does not support item assignment
>>>
```

**Todas las operaciones y métodos que manipulan los datos de una cadena, siempre crean nuevas cadenas.**
