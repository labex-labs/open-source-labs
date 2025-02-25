# Ejercicio 2.8: Cómo formatear números

Un problema común al imprimir números es especificar el número de decimales. Una forma de solucionarlo es usar `f-strings`. Prueba estos ejemplos:

```python
>>> valor = 42863.1
>>> print(valor)
42863.1
>>> print(f'{valor:0.4f}')
42863.1000
>>> print(f'{valor:>16.2f}')
        42863.10
>>> print(f'{valor:<16.2f}')
42863.10
>>> print(f'{valor:*>16,.2f}')
*******42,863.10
>>>
```

La documentación completa sobre los códigos de formateo utilizados en `f-strings` se puede encontrar [aquí](https://docs.python.org/3/library/string.html#format-specification-mini-language). A veces, el formateo también se realiza utilizando el operador `%` de cadenas.

```python
>>> print('%0.4f' % valor)
42863.1000
>>> print('%16.2f' % valor)
        42863.10
>>>
```

La documentación sobre los diversos códigos utilizados con `%` se puede encontrar [aquí](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

Aunque se utiliza comúnmente con `print`, el formateo de cadenas no está vinculado a la impresión. Si quieres guardar una cadena formateada, simplemente asígnala a una variable.

```python
>>> f = '%0.4f' % valor
>>> f
'42863.1000'
>>>
```
