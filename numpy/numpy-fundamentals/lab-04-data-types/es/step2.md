# Trabajando con Tipos de Datos

Los tipos de datos de NumPy se representan como objetos `dtype` (tipo de datos). Una vez que has importado NumPy usando `import numpy as np`, puedes acceder a los tipos de datos usando `np.bool_`, `np.float32`, etc.

Puedes usar los tipos de datos como funciones para convertir números de Python en escalares de matriz, secuencias de números de Python en matrices de ese tipo o como argumentos para la palabra clave dtype en muchas funciones o métodos de NumPy. Aquí hay algunos ejemplos:

```python
x = np.float32(1.0)
# x es ahora un escalar de matriz de tipo float32 con el valor 1.0

y = np.int_([1,2,4])
# y es ahora una matriz de enteros con los valores [1, 2, 4]

z = np.arange(3, dtype=np.uint8)
# z es ahora una matriz de tipo uint8 con los valores [0, 1, 2]
```

También puedes referirte a los tipos de matriz usando códigos de carácter, aunque se recomienda usar objetos dtype en su lugar. Por ejemplo:

```python
np.array([1, 2, 3], dtype='f')
# devuelve una matriz con los valores [1., 2., 3.] y dtype float32
```

Para convertir el tipo de una matriz, puedes usar el método `.astype()` o el tipo mismo como una función. Por ejemplo:

```python
z.astype(float)
# devuelve la matriz z con dtype float64

np.int8(z)
# devuelve la matriz z con dtype int8
```
