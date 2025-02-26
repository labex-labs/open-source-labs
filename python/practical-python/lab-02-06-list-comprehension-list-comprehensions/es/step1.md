# Creando nuevas listas

Una comprensión de lista crea una nueva lista aplicando una operación a cada elemento de una secuencia.

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a ]
>>> b
[2, 4, 6, 8, 10]
>>>
```

Otro ejemplo:

```python
>>> names = ['Elwood', 'Jake']
>>> a = [name.lower() for name in names]
>>> a
['elwood', 'jake']
>>>
```

La sintaxis general es: `[ <expresión> for <nombre_variable> in <secuencia> ]`.
