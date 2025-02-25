# Entrada y salida de archivos

Abrir un archivo.

```python
f = open('foo.txt', 'rt')     # Abrir para lectura (texto)
g = open('bar.txt', 'wt')     # Abrir para escritura (texto)
```

Leer todos los datos.

```python
data = f.read()

# Leer solo hasta 'maxbytes' bytes
data = f.read([maxbytes])
```

Escribir algunos textos.

```python
g.write('algun texto')
```

Cerrar cuando hayas terminado.

```python
f.close()
g.close()
```

Los archivos deben cerrarse correctamente y es fácil olvidarse de este paso. Por lo tanto, el enfoque preferido es usar la declaración `with` de la siguiente manera.

```python
with open(nombre_archivo, 'rt') as archivo:
    # Usar el archivo `archivo`
  ...
    # No es necesario cerrar explícitamente
...instrucciones
```

Esto cierra automáticamente el archivo cuando el control sale del bloque de código con sangría.
