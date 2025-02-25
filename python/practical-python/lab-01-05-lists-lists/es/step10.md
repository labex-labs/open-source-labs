# Ejercicio 1.22: Agregar, insertar y eliminar elementos

Utiliza el método `append()` para agregar el símbolo `'RHT'` al final de `symlist`.

```python
>>> symlist.append('RHT') # agrega 'RHT'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Utiliza el método `insert()` para insertar el símbolo `'AA'` como el segundo elemento de la lista.

```python
>>> symlist.insert(1, 'AA') # Inserta 'AA' como el segundo elemento de la lista
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Utiliza el método `remove()` para eliminar `'MSFT'` de la lista.

```python
>>> symlist.remove('MSFT') # Elimina 'MSFT'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
>>>
```

Agrega una entrada duplicada de `'YHOO'` al final de la lista.

_Nota: está perfectamente bien que una lista tenga valores duplicados._

```python
>>> symlist.append('YHOO') # Agrega 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT', 'YHOO']
>>>
```

Utiliza el método `index()` para encontrar la primera posición de `'YHOO'` en la lista.

```python
>>> symlist.index('YHOO') # Encuentra el primer índice de 'YHOO'
4
>>> symlist[4]
'YHOO'
>>>
```

Cuenta cuántas veces aparece `'YHOO'` en la lista:

```python
>>> symlist.count('YHOO')
2
>>>
```

Elimina la primera aparición de `'YHOO'`.

```python
>>> symlist.remove('YHOO') # Elimina la primera aparición de 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'GOOG', 'RHT', 'YHOO']
>>>
```

Para que lo sepas, no hay ningún método para encontrar o eliminar todas las apariciones de un elemento. Sin embargo, veremos una forma elegante de hacer esto en la sección 2.
