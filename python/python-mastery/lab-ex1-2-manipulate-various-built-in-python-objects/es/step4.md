# Trabajando con diccionarios en Python

En Python, los diccionarios son una estructura de datos fundamental. Son almacenes de pares clave - valor, lo que significa que te permiten asociar un valor (el valor) con otro (la clave). Esto es extremadamente útil cuando se trabaja con datos que tienen relaciones naturales de clave - valor. Por ejemplo, podrías querer asociar el nombre de una persona (la clave) con su edad (el valor), o como veremos en este laboratorio, asociar símbolos de acciones (claves) con sus precios (valores).

## Creación y acceso a diccionarios

Comencemos abriendo una nueva sesión interactiva de Python. Esto es como entrar en un entorno especial donde puedes escribir y ejecutar código Python línea por línea. Para iniciar esta sesión, abre tu terminal y escribe el siguiente comando:

```bash
python3
```

Una vez que estés en la sesión interactiva de Python, puedes crear un diccionario. En nuestro caso, crearemos un diccionario que asocia símbolos de acciones con sus precios. Así es como se hace:

```python
>>> prices = {'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
>>> prices
{'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
```

En la primera línea, estamos creando un diccionario llamado `prices` y asignándole algunos pares clave - valor. Las claves son los símbolos de acciones (`IBM`, `GOOG`, `AAPL`), y los valores son los precios correspondientes. La segunda línea simplemente nos muestra el contenido del diccionario `prices`.

Ahora, veamos cómo acceder y modificar los valores en el diccionario utilizando las claves.

```python
>>> prices['IBM']    # Acceder al valor para la clave 'IBM'
91.1

>>> prices['IBM'] = 123.45    # Actualizar un valor existente
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23}

>>> prices['HPQ'] = 26.15    # Agregar un nuevo par clave - valor
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23, 'HPQ': 26.15}
```

En la primera línea, estamos accediendo al valor asociado con la clave `IBM`. En la segunda y tercera líneas, estamos actualizando el valor para la clave `IBM` y luego agregando un nuevo par clave - valor (`HPQ` con un precio de `26.15`).

## Obtener las claves de un diccionario

A veces, es posible que desees obtener una lista de todas las claves de un diccionario. Hay un par de formas de hacer esto.

```python
>>> list(prices)    # Convertir las claves del diccionario en una lista
['IBM', 'GOOG', 'AAPL', 'HPQ']
```

Aquí, estamos usando la función `list()` para convertir las claves del diccionario `prices` en una lista.

También puedes usar el método `keys()`, que devuelve un objeto especial llamado `dict_keys`.

```python
>>> prices.keys()    # Devuelve un objeto dict_keys
dict_keys(['IBM', 'GOOG', 'AAPL', 'HPQ'])
```

## Obtener los valores de un diccionario

De manera similar, es posible que desees obtener todos los valores de un diccionario. Puedes usar el método `values()` para esto.

```python
>>> prices.values()    # Devuelve un objeto dict_values
dict_values([123.45, 490.1, 312.23, 26.15])
```

Este método devuelve un objeto `dict_values` que contiene todos los valores del diccionario `prices`.

## Eliminar elementos

Si deseas eliminar un par clave - valor de un diccionario, puedes usar la palabra clave `del`.

```python
>>> del prices['AAPL']    # Eliminar la entrada 'AAPL'
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'HPQ': 26.15}
```

Aquí, estamos eliminando el par clave - valor con la clave `AAPL` del diccionario `prices`.

## Comprobar si una clave existe

Para comprobar si una clave existe en un diccionario, puedes usar el operador `in`.

```python
>>> 'IBM' in prices
True
>>> 'AAPL' in prices
False
```

El operador `in` devuelve `True` si la clave existe en el diccionario y `False` en caso contrario.

## Métodos de diccionarios

Los diccionarios tienen varios métodos útiles. Veamos un par de ellos.

```python
>>> prices.get('MSFT', 0)    # Obtener el valor o un valor predeterminado si la clave no existe
0
>>> prices.get('IBM', 0)
123.45

>>> prices.update({'MSFT': 25.0, 'GOOG': 500.0})    # Actualizar múltiples valores
>>> prices
{'IBM': 123.45, 'GOOG': 500.0, 'HPQ': 26.15, 'MSFT': 25.0}
```

El método `get()` intenta obtener el valor asociado con una clave. Si la clave no existe, devuelve un valor predeterminado (en este caso, `0`). El método `update()` se utiliza para actualizar múltiples pares clave - valor en el diccionario a la vez.

Cuando hayas terminado de trabajar en la sesión interactiva de Python, puedes salir de ella escribiendo:

```python
>>> exit()
```
