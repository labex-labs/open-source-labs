# Ejercicio 1.28: Otros tipos de "archivos"

¿Qué pasa si quieres leer un archivo no de texto, como un archivo de datos comprimido con gzip? La función `open()` incorporada no te ayudará aquí, pero Python tiene un módulo de biblioteca `gzip` que puede leer archivos comprimidos con gzip.

Prueba:

```python
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')

... mira la salida...
>>>
```

Nota: Incluir el modo de archivo de `'rt'` es fundamental aquí. Si lo olvidas, obtendrás cadenas de bytes en lugar de cadenas de texto normales.
