# Usando la función map()

En Python, una función de orden superior es una función que puede tomar otra función como argumento o devolver una función como resultado. La función `map()` de Python es un excelente ejemplo de función de orden superior. Es una herramienta poderosa que te permite aplicar una función dada a cada elemento de un iterable, como una lista o una tupla. Después de aplicar la función a cada elemento, devuelve un iterador con los resultados. Esta característica hace que `map()` sea perfecta para procesar secuencias de datos, como las filas de un archivo CSV.

La sintaxis básica de la función `map()` es la siguiente:

```python
map(function, iterable, ...)
```

Aquí, la `function` es la operación que quieres realizar en cada elemento del `iterable`. El `iterable` es una secuencia de elementos, como una lista o una tupla.

Veamos un ejemplo sencillo. Supongamos que tienes una lista de números y quieres elevar al cuadrado cada número de esa lista. Puedes usar la función `map()` para lograr esto. Así es como se hace:

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

En este ejemplo, primero definimos una lista llamada `numbers`. Luego, usamos la función `map()`. La función `lambda` `lambda x: x * x` es la operación que queremos realizar en cada elemento de la lista `numbers`. La función `map()` aplica esta función `lambda` a cada número de la lista. Dado que `map()` devuelve un iterador, lo convertimos a una lista usando la función `list()`. Finalmente, imprimimos la lista `squared`, que contiene los valores al cuadrado de los números originales.

Ahora, veamos cómo podemos usar la función `map()` para modificar nuestra función `convert_csv()`. Anteriormente, usamos un bucle `for` para iterar sobre las filas de los datos CSV. Ahora, reemplazaremos ese bucle `for` con la función `map()`.

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function
    '''
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)

    # Use map to apply conversion_func to each row
    records = list(map(lambda row: conversion_func(headers, row), rows))
    return records
```

Esta versión actualizada de la función `convert_csv()` hace exactamente lo mismo que la versión anterior, pero utiliza la función `map()` en lugar de un bucle `for`. La función `lambda` dentro de `map()` toma cada fila de los datos CSV y le aplica la `conversion_func`, junto con los encabezados.

Probemos esta función actualizada para asegurarnos de que funcione correctamente. Primero, abre tu terminal y navega hasta el directorio del proyecto. Luego, inicia la shell interactiva de Python con el archivo `reader.py`.

```bash
cd ~/project
python3 -i reader.py
```

Una vez que estés en la shell de Python, ejecuta el siguiente código para probar la función `convert_csv()` actualizada:

```python
# Test the updated convert_csv function
with open('portfolio.csv') as f:
    result = convert_csv(f, make_dict)
print(result[0])  # Should print the first dictionary

# Test that csv_as_dicts still works
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # Should print the first dictionary with converted types
```

Después de ejecutar este código, deberías ver una salida similar a la siguiente:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Esta salida muestra que la función `convert_csv()` actualizada que utiliza la función `map()` funciona correctamente, y las funciones que dependen de ella también siguen funcionando como se espera.

Usar la función `map()` tiene varias ventajas:

1. Puede ser más concisa que un bucle `for`. En lugar de escribir varias líneas de código para un bucle `for`, puedes lograr el mismo resultado con una sola línea usando `map()`.
2. Comunica claramente tu intención de transformar cada elemento de una secuencia. Cuando ves `map()`, inmediatamente sabes que estás aplicando una función a cada elemento de un iterable.
3. Puede ser más eficiente en términos de memoria porque devuelve un iterador. Un iterador genera valores sobre la marcha, lo que significa que no almacena todos los resultados en memoria a la vez. En nuestro ejemplo, convertimos el iterador devuelto por `map()` a una lista, pero en algunos casos, puedes trabajar directamente con el iterador para ahorrar memoria.

Para salir de la shell de Python, puedes escribir `exit()` o presionar Ctrl+D.
