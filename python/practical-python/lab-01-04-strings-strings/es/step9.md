# Cadenas de bytes

Una cadena de bytes de 8 bits, comúnmente encontrada en la E/S de bajo nivel, se escribe de la siguiente manera:

```python
data = b'Hello World\r\n'
```

Al poner una pequeña `b` antes de la primera comilla, se especifica que es una cadena de bytes en oposición a una cadena de texto.

La mayoría de las operaciones habituales de cadenas funcionan.

```python
len(data)                         # 13
data[0:5]                         # b'Hello'
data.replace(b'Hello', b'Cruel')  # b'Cruel World\r\n'
```

La indexación es un poco diferente porque devuelve valores de byte como enteros.

```python
data[0]   # 72 (código ASCII para 'H')
```

Conversión a/desde cadenas de texto.

```python
text = data.decode('utf-8') # bytes -> texto
data = text.encode('utf-8') # texto -> bytes
```

El argumento `'utf-8'` especifica una codificación de caracteres. Otros valores comunes incluyen `'ascii'` y `'latin1'`.
