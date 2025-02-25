# Tipos de datos de secuencia

Python tiene tres tipos de datos de _secuencia_.

- Cadena: `'Hola'`. Una cadena es una secuencia de caracteres.
- Lista: `[1, 4, 5]`.
- Tupla: `('GOOG', 100, 490.1)`.

Todas las secuencias están ordenadas, indexadas por enteros y tienen una longitud.

```python
a = 'Hola'               # Cadena
b = [1, 4, 5]             # Lista
c = ('GOOG', 100, 490.1)  # Tupla

# Orden indexado
a[0]                      # 'H'
b[-1]                     # 5
c[1]                      # 100

# Longitud de la secuencia
len(a)                    # 5
len(b)                    # 3
len(c)                    # 3
```

Las secuencias se pueden replicar: `s * n`.

```python
>>> a = 'Hola'
>>> a * 3
'HolaHolaHola'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

Las secuencias del mismo tipo se pueden concatenar: `s + t`.

```python
>>> a = (1, 2, 3)
>>> b = (4, 5)
>>> a + b
(1, 2, 3, 4, 5)
>>>
>>> c = [1, 5]
>>> a + c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: solo se puede concatenar tupla (no "lista") a tupla
```
