# Ejercicio 1.13: Extracción de caracteres individuales y subcadenas

Las cadenas son arrays de caracteres. Intenta extraer algunos caracteres:

```python
>>> symbols[0]
?
>>> symbols[1]
?
>>> symbols[2]
?
>>> symbols[-1]        # Último carácter
?
>>> symbols[-2]        # Los índices negativos son a partir del final de la cadena
?
>>>
```

En Python, las cadenas son de solo lectura.

Verifícalo intentando cambiar el primer carácter de `symbols` a una 'a' en minúsculas.

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```
