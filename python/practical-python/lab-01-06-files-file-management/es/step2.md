# Expresiones habituales para leer datos de archivos

Leer todo un archivo de una vez como una cadena.

```python
with open('foo.txt', 'rt') as archivo:
    datos = archivo.read()
    # `datos` es una cadena con todo el texto de `foo.txt`
```

Leer un archivo línea por línea mediante iteración.

```python
with open(nombre_archivo, 'rt') as archivo:
    for linea in archivo:
        # Procesar la línea
```
