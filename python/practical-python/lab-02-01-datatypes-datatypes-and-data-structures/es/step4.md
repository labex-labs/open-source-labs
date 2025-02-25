# Tuplas

Una tupla es una colección de valores agrupados juntos.

Ejemplo:

```python
s = ('GOOG', 100, 490.1)
```

A veces se omiten los `()` en la sintaxis.

```python
s = 'GOOG', 100, 490.1
```

Casos especiales (tupla de 0 elementos, tupla de 1 elemento).

```python
t = ()            # Una tupla vacía
w = ('GOOG', )    # Una tupla con 1 elemento
```

Las tuplas se utilizan a menudo para representar registros o estructuras _simples_. Típicamente, es un solo _objeto_ con múltiples partes. Una buena analogía: _Una tupla es como una sola fila en una tabla de base de datos_.

Los contenidos de la tupla están ordenados (como una matriz).

```python
s = ('GOOG', 100, 490.1)
name = s[0]                 # 'GOOG'
shares = s[1]               # 100
price = s[2]                # 490.1
```

Sin embargo, los contenidos no se pueden modificar.

```python
>>> s[1] = 75
TypeError: object does not support item assignment
```

Sin embargo, se puede crear una nueva tupla basada en una tupla actual.

```python
s = (s[0], 75, s[2])
```
