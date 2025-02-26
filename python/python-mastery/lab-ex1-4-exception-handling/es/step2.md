# Agregando manejo de errores

Cuando se escriben programas que procesan datos, es común encontrar errores relacionados con datos incorrectos (malformados, campos faltantes, etc.). Modifique su programa `pcost.py` para leer el archivo de datos `portfolio3.dat` y ejecútelo (pista: debe detenerse).

Modifique ligeramente su función para que sea capaz de recuperarse de líneas con datos incorrectos. Por ejemplo, las funciones de conversión `int()` y `float()` generan una excepción `ValueError` si no pueden convertir la entrada. Utilice `try` y `except` para capturar e imprimir un mensaje de advertencia sobre las líneas que no se pueden analizar. Por ejemplo:

```shell
No se pudo analizar: 'C - 53.08\n'
Razón: literal no válido para int() con base 10: '-'
No se pudo analizar: 'DIS - 34.20\n'
Razón: literal no válido para int() con base 10: '-'
...
```

Intente ejecutar nuevamente su programa en el archivo `portfolio3.dat`. Debería ejecutarse correctamente a pesar de los mensajes de advertencia impresos.
