# El papel de las clases

Las definiciones que componen una definición de clase son compartidas por todas las instancias de esa clase. Observe que todas las instancias tienen un enlace de regreso a su clase asociada:

```python
>>> goog.__class__
... observe la salida...
>>> ibm.__class__
... observe la salida...
>>>
```

Intente llamar a un método en las instancias:

```python
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
>>>
```

Observe que el nombre 'cost' no está definido en `goog.__dict__` ni en `ibm.__dict__`. En su lugar, está siendo suministrado por el diccionario de la clase. Pruebe esto:

```python
>>> SimpleStock.__dict__['cost']
... observe la salida...
>>>
```

Intente llamar al método `cost()` directamente a través del diccionario:

```python
>>> SimpleStock.__dict__['cost'](goog)
49010.00
>>> SimpleStock.__dict__['cost'](ibm)
4561.5
>>>
```

Observe cómo está llamando a la función definida en la definición de clase y cómo el argumento `self` obtiene la instancia.

Si agrega un nuevo valor a la clase, se convierte en una variable de clase que es visible para todas las instancias. Pruebe:

```python
>>> SimpleStock.spam = 42
>>> ibm.spam
42
>>> goog.spam
42
>>>
```

Observe que `spam` no es parte del diccionario de la instancia.

```python
>>> ibm.__dict__
... observe la salida...
>>>
```

En su lugar, es parte del diccionario de la clase:

```python
>>> SimpleStock.__dict__['spam']
42
>>>
```

Esencialmente, esto es todo lo que realmente es una clase: es una colección de valores compartidos por las instancias.
