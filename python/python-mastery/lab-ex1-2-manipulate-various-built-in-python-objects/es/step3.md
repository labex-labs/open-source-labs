# Trabajando con listas en Python

Las listas son un tipo de estructura de datos en Python. Una estructura de datos es una forma de organizar y almacenar datos para que se puedan utilizar de manera eficiente. Las listas son muy versátiles porque pueden almacenar diferentes tipos de elementos, como números, cadenas (strings) o incluso otras listas. En este paso, aprenderemos cómo realizar diversas operaciones en listas.

## Creación de listas a partir de cadenas

Para comenzar a trabajar con listas en Python, primero debemos abrir una sesión interactiva de Python. Esto es como un entorno especial donde podemos escribir y ejecutar código Python de inmediato. Para iniciar esta sesión, escribe el siguiente comando en tu terminal:

```bash
python3
```

Una vez que estés en la sesión interactiva de Python, crearemos una lista a partir de una cadena. Una cadena es simplemente una secuencia de caracteres. Definiremos una cadena que contiene algunos símbolos de acciones separados por espacios. Luego, convertiremos esta cadena en una lista. Cada símbolo de acción se convertirá en un elemento de la lista.

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO GOOG'
>>> symlist = symbols.split()    # Dividir la cadena en espacios en blanco
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG']
```

El método `split()` se utiliza para dividir la cadena en partes siempre que haya un espacio en blanco. Cada parte se convierte entonces en un elemento de la nueva lista.

## Acceso y modificación de elementos de la lista

Al igual que las cadenas, las listas admiten la indexación. La indexación significa que podemos acceder a elementos individuales de la lista por su posición. En Python, el primer elemento de una lista tiene un índice de 0, el segundo tiene un índice de 1, y así sucesivamente. También podemos usar la indexación negativa para acceder a elementos desde el final de la lista. El último elemento tiene un índice de -1, el penúltimo tiene un índice de -2, y así sucesivamente.

A diferencia de las cadenas, los elementos de la lista se pueden modificar. Esto significa que podemos cambiar el valor de un elemento de la lista.

```python
>>> symlist[0]    # Primer elemento
'HPQ'
>>> symlist[1]    # Segundo elemento
'AAPL'
>>> symlist[-1]   # Último elemento
'GOOG'
>>> symlist[-2]   # Penúltimo elemento
'YHOO'

>>> symlist[2] = 'AIG'    # Reemplazar el tercer elemento
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
```

## Iteración a través de listas

A menudo, necesitamos realizar la misma operación en cada elemento de una lista. Podemos usar un bucle `for` para hacer esto. Un bucle `for` nos permite recorrer cada elemento de la lista uno por uno y realizar una acción específica en él.

```python
>>> for s in symlist:
...     print('s =', s)
...
```

Cuando ejecutes este código, verás cada elemento de la lista impreso con la etiqueta `s =`.

```
s = HPQ
s = AAPL
s = AIG
s = MSFT
s = YHOO
s = GOOG
```

## Comprobación de pertenencia

A veces, necesitamos comprobar si un elemento en particular existe en una lista. Podemos usar el operador `in` para hacer esto. El operador `in` devuelve `True` si el elemento está en la lista y `False` si no lo está.

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>> 'CAT' in symlist
False
```

## Adición y eliminación de elementos

Las listas tienen métodos incorporados que nos permiten agregar y eliminar elementos. El método `append()` agrega un elemento al final de la lista. El método `insert()` inserta un elemento en una posición específica de la lista. El método `remove()` elimina un elemento de la lista por su valor.

```python
>>> symlist.append('RHT')    # Agregar un elemento al final
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.insert(1, 'AA')    # Insertar en una posición específica
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.remove('MSFT')    # Eliminar por valor
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

Si intentas eliminar un elemento que no existe en la lista, Python generará un error.

```python
>>> symlist.remove('MSFT')
```

Verás un mensaje de error como este:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

También podemos encontrar la posición de un elemento en la lista utilizando el método `index()`.

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]    # Verificar el elemento en esa posición
'YHOO'
```

## Ordenación de listas

Las listas se pueden ordenar in situ, lo que significa que la lista original se modifica. Podemos ordenar una lista alfabéticamente o en orden inverso.

```python
>>> symlist.sort()    # Ordenar alfabéticamente
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']

>>> symlist.sort(reverse=True)    # Ordenar en orden inverso
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
```

## Listas anidadas

Las listas pueden contener cualquier tipo de objeto, incluyendo otras listas. Esto se llama una lista anidada.

```python
>>> nums = [101, 102, 103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Para acceder a elementos en una lista anidada, usamos múltiples índices. El primer índice selecciona el elemento de la lista exterior, y el segundo índice selecciona el elemento de la lista interior.

```python
>>> items[0]    # Primer elemento (la lista symlist)
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]    # Segundo elemento en symlist
'RHT'
>>> items[0][1][2]    # Tercer carácter en 'RHT'
'T'
>>> items[1]    # Segundo elemento (la lista nums)
[101, 102, 103]
>>> items[1][1]    # Segundo elemento en nums
102
```

Cuando hayas terminado de trabajar en la sesión interactiva de Python, puedes salir de ella escribiendo:

```python
>>> exit()
```
