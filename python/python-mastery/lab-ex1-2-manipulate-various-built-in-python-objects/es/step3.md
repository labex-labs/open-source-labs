# Parte 3 : Manipulación de Listas

En la primera parte, trabajó con cadenas que contenían símbolos de acciones. Por ejemplo:

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO  GOOG'
>>>
```

Defina la variable anterior y divídala en una lista de nombres utilizando la operación `split()` de cadenas:

```python
>>> symlist = symbols.split()
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG' ]
>>>
```

## Extracción y reasignación de elementos de lista

Las listas funcionan como arrays donde puede buscar y modificar elementos por índice numérico. Pruebe algunas búsquedas:

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'YHOO'
>>>
```

Pruebe reasignar uno de los elementos:

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG' ]
>>>
```

## Bucle sobre los elementos de la lista

El bucle `for` funciona recorriendo datos en una secuencia como una lista. Verifíquelo escribiendo el siguiente bucle y observando lo que sucede:

```python
>>> for s in symlist:
        print('s =', s)

... observe la salida...
```

## Pruebas de pertenencia

Utilice el operador `in` para comprobar si `'AIG'`, `'AA'` y `'CAT'` están en la lista de símbolos.

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>>
```

## Anexar, insertar y eliminar elementos

Utilice el método `append()` para agregar el símbolo `'RHT'` al final de `symlist`.

```python
>>> symlist.append('RHT')
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Utilice el método `insert()` para insertar el símbolo `'AA'` como el segundo elemento de la lista.

```python
>>> symlist.insert(1,'AA')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Utilice el método `remove()` para eliminar `'MSFT'` de la lista.

```python
>>> symlist.remove('MSFT')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

Pruebe llamar a `remove()` nuevamente para ver lo que sucede si el elemento no se puede encontrar.

```python
>>> symlist.remove('MSFT')
... observe lo que sucede...
>>>
```

Utilice el método `index()` para encontrar la posición de `'YHOO'` en la lista.

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]
'YHOO'
>>>
```

## Ordenamiento de listas

¿Quiere ordenar una lista? Utilice el método `sort()`. Pruebe:

```python
>>> symlist.sort()
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']
>>>
```

¿Quiere ordenar en orden inverso? Pruebe esto:

```python
>>> symlist.sort(reverse=True)
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>>
```

Nota: Ordenar una lista modifica su contenido "in-place". Es decir, los elementos de la lista se reorganizan, pero no se crea una nueva lista como resultado.

## Listas de cualquier cosa

Las listas pueden contener cualquier tipo de objeto, incluyendo otras listas (por ejemplo, listas anidadas). Pruebe:

```python
>>> nums = [101,102,103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Presta mucha atención a la salida anterior. `items` es una lista con dos elementos. Cada elemento es una lista.

Pruebe algunas búsquedas en listas anidadas:

```python
>>> items[0]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]
'RHT'
>>> items[0][1][2]
'T'
>>> items[1]
[101, 102, 103]
>>> items[1][1]
102
>>>
```
