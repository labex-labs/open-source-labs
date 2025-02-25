# Función zip()

La función `zip` toma múltiples secuencias y crea un iterador que las combina.

```python
columns = ['name','shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
# ('name','GOOG'), ('shares',100), ('price',490.1)
```

Para obtener el resultado, debes iterar. Puedes usar múltiples variables para desempaquetar las tuplas como se mostró anteriormente.

```python
for column, value in pairs:
 ...
```

Un uso común de `zip` es crear pares clave/valor para construir diccionarios.

```python
d = dict(zip(columns, values))
```
