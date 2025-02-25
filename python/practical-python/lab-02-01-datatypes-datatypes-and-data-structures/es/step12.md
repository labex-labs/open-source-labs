# Ejercicio 2.2: Diccionarios como estructura de datos

Una alternativa a una tupla es crear un diccionario en su lugar.

```python
>>> d = {
        'name' : row[0],
       'shares' : int(row[1]),
        'price'  : float(row[2])
    }
>>> d
{'name': 'AA','shares': 100, 'price': 32.2 }
>>>
```

Calcula el costo total de esta cartera:

```python
>>> cost = d['shares'] * d['price']
>>> cost
3220.0000000000005
>>>
```

Compara este ejemplo con el mismo cálculo que involucra tuplas arriba. Cambia el número de acciones a 75.

```python
>>> d['shares'] = 75
>>> d
{'name': 'AA','shares': 75, 'price': 32.2 }
>>>
```

A diferencia de las tuplas, los diccionarios se pueden modificar libremente. Agrega algunos atributos:

```python
>>> d['date'] = (6, 11, 2007)
>>> d['account'] = 12345
>>> d
{'name': 'AA','shares': 75, 'price':32.2, 'date': (6, 11, 2007), 'account': 12345}
>>>
```
