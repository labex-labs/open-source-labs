# Tamaño en bytes de una cadena

## Problema

Escribe una función `byte_size(s)` que tome una cadena `s` como entrada y devuelva su tamaño en bytes. El tamaño en bytes de una cadena es el número de bytes necesarios para almacenar la cadena en memoria. Para calcular el tamaño en bytes de una cadena, debes codificar la cadena utilizando un esquema de codificación específico. En este desafío, utilizarás el esquema de codificación UTF-8.

Para calcular el tamaño en bytes de una cadena, puedes seguir estos pasos:

1. Codifica la cadena utilizando el esquema de codificación UTF-8.
2. Obtén la longitud de la cadena codificada.

Tu función debe devolver la longitud de la cadena codificada.

## Ejemplo

```python
byte_size('😀') # 4
byte_size('Hello World') # 11
```

En el ejemplo anterior, el tamaño en bytes de la cadena `'😀'` es 4 porque se necesitan 4 bytes para almacenar la versión codificada en UTF-8 de la cadena en memoria. El tamaño en bytes de la cadena `'Hello World'` es 11 porque se necesitan 11 bytes para almacenar la versión codificada en UTF-8 de la cadena en memoria.
