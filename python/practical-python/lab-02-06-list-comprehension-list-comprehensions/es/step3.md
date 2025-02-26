# Casos de uso

Las comprensiones de lista son muy útiles. Por ejemplo, puedes recopilar los valores de un campo específico de un diccionario:

```python
stocknames = [s['name'] for s in stocks]
```

Puedes realizar consultas similares a las de una base de datos en secuencias.

```python
a = [s for s in stocks if s['price'] > 100 and s['shares'] > 50 ]
```

También puedes combinar una comprensión de lista con una reducción de secuencia:

```python
cost = sum([s['shares']*s['price'] for s in stocks])
```
