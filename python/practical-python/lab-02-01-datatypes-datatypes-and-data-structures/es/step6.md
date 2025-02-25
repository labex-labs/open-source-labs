# Desempaquetado de tuplas

Para usar la tupla en otro lugar, se pueden desempaquetar sus partes en variables.

```python
name, shares, price = s
print('Cost', shares * price)
```

El número de variables en el lado izquierdo debe coincidir con la estructura de la tupla.

```python
name, shares = s     # ERROR
Traceback (most recent call last):
...
ValueError: too many values to unpack
```
