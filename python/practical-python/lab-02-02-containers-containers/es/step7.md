# Claves Compuestas

Casi cualquier tipo de valor puede usarse como clave de un diccionario en Python. La clave de un diccionario debe ser de un tipo inmutable. Por ejemplo, tuplas:

```python
holidays = {
  (1, 1) : 'New Years',
  (3, 14) : 'Pi day',
  (9, 13) : "Programmer's day",
}
```

Luego, para acceder:

```python
>>> holidays[3, 14]
'Pi day'
>>>
```

_Ni una lista, ni un conjunto, ni otro diccionario pueden servir como clave de un diccionario, porque las listas y los diccionarios son mutables._
