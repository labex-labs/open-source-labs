# Rellenar cadena

## Problema

Escribe una función `pad(s: str, length: int, char: str ='') -> str` que rellene una cadena con el carácter especificado en ambos lados, si es más corta que la longitud especificada. La función debe recibir tres parámetros:

- `s`: una cadena que necesita ser rellenada
- `length`: un entero que especifica la longitud total de la cadena rellena
- `char`: un carácter que se utiliza para rellenar la cadena. El valor predeterminado es un carácter de espacio en blanco.

La función debe devolver la cadena rellena.

## Ejemplo

```python
pad('cat', 8) #' cat   '
pad('42', 6, '0') # '004200'
pad('foobar', 3) # 'foobar'
```
