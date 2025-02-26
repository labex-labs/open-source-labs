# Ejercicio 5.4: Métodos vinculados

Una característica sutil de Python es que invocar un método implica dos pasos y algo conocido como un método vinculado. Por ejemplo:

```python
>>> s = goog.sell
>>> s
<bound method Stock.sell of Stock('GOOG', 100, 490.1)>
>>> s(25)
>>> goog.shares
75
>>>
```

Los métodos vinculados en realidad contienen todas las piezas necesarias para llamar a un método. Por ejemplo, guardan un registro de la función que implementa el método:

```python
>>> s.__func__
<function sell at 0x10049af50>
>>>
```

Este es el mismo valor que se encuentra en el diccionario de `Stock`.

```python
>>> Stock.__dict__['sell']
<function sell at 0x10049af50>
>>>
```

Los métodos vinculados también registran la instancia, que es el argumento `self`.

```python
>>> s.__self__
Stock('GOOG',75,490.1)
>>>
```

Cuando se invoca la función usando `()`, todas las piezas se unen. Por ejemplo, llamar `s(25)` en realidad hace esto:

```python
>>> s.__func__(s.__self__, 25)    # Lo mismo que s(25)
>>> goog.shares
50
>>>
```
