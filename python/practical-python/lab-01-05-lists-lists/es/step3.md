# Iteración y búsqueda en listas

Utiliza `for` para iterar sobre los contenidos de la lista.

```python
for name in names:
    # utiliza name
    # por ejemplo, print(name)
  ...
```

Esto es similar a una declaración `foreach` de otros lenguajes de programación.

Para encontrar rápidamente la posición de algo, utiliza `index()`.

```python
names = ['Elwood','Jake','Curtis']
names.index('Curtis')   # 2
```

Si el elemento está presente más de una vez, `index()` devolverá el índice de la primera aparición.

Si el elemento no se encuentra, se generará una excepción `ValueError`.
