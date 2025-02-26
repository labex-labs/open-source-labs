# Ejercicio 2.20: Reducciones de secuencia

Calcula el costo total de la cartera utilizando una sola instrucción de Python.

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> cost = sum([ s['shares'] * s['price'] for s in portfolio ])
>>> cost
44671.15
>>>
```

Una vez que hayas hecho eso, muestra cómo puedes calcular el valor actual de la cartera utilizando una sola instrucción.

```python
>>> value = sum([ s['shares'] * prices[s['name']] for s in portfolio ])
>>> value
28686.1
>>>
```

Ambas operaciones anteriores son un ejemplo de map-reduce. La comprensión de lista está aplicando una operación a través de la lista.

```python
>>> [ s['shares'] * s['price'] for s in portfolio ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
>>>
```

La función `sum()` luego está realizando una reducción en el resultado:

```python
>>> sum(_)
44671.15
>>>
```

Con este conocimiento, ya estás listo para lanzar una empresa de startups de big data.
