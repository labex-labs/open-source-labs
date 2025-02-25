# Construcción de Diccionarios

Ejemplo de construcción de un diccionario desde cero.

```python
prices = {} # Diccionario vacío inicial

# Insertar nuevos elementos
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37
```

Un ejemplo de llenado del diccionario a partir del contenido de un archivo.

```python
prices = {} # Diccionario vacío inicial

with open('prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        prices[row[0]] = float(row[1])
```

Nota: Si intenta esto con el archivo `prices.csv`, encontrará que casi funciona, pero hay una línea en blanco al final que hace que se detenga. Tendrá que encontrar alguna manera de modificar el código para tener en cuenta eso (ver Ejercicio 2.6).
