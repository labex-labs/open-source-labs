# Función enumerate()

La función `enumerate` agrega un valor de contador adicional a la iteración.

```python
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    # Bucle con i = 0, name = 'Elwood'
    # i = 1, name = 'Jake'
    # i = 2, name = 'Curtis'
```

La forma general es `enumerate(secuencia [, start = 0])`. `start` es opcional. Un buen ejemplo de uso de `enumerate()` es el seguimiento de números de línea mientras se lee un archivo:

```python
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
     ...
```

Al final, `enumerate` es simplemente un atajo práctico para:

```python
i = 0
for x in s:
    statements
    i += 1
```

Usar `enumerate` implica menos tecleo y es un poco más rápido.
