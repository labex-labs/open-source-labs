# Idea Profunda: "Duck Typing"

[Duck Typing](https://en.wikipedia.org/wiki/Duck_typing) es un concepto de programación informática para determinar si un objeto puede ser utilizado con un propósito particular. Es una aplicación de la [prueba del pato](https://en.wikipedia.org/wiki/Duck_test).

> Si parece un pato, nada como un pato y cuac como un pato, entonces probablemente es un pato.

En la segunda versión de `read_data()` arriba, la función espera cualquier objeto iterable. No solo las líneas de un archivo.

```python
def read_data(lines):
    records = []
    for line in lines:
     ...
        records.append(r)
    return records
```

Esto significa que podemos utilizarlo con otras _líneas_.

```python
# Un archivo CSV
lines = open('data.csv')
data = read_data(lines)

# Un archivo comprimido
lines = gzip.open('data.csv.gz','rt')
data = read_data(lines)

# La Entrada Estándar
lines = sys.stdin
data = read_data(lines)

# Una lista de cadenas
lines = ['ACME,50,91.1','IBM,75,123.45',...]
data = read_data(lines)
```

Hay una gran flexibilidad con este diseño.

_Pregunta: ¿Debemos aceptar o combatir esta flexibilidad?_
