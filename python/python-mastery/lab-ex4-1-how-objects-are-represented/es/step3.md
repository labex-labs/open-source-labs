# Modificación de los Datos de la Instancia

Intente establecer un nuevo atributo en una de las instancias anteriores:

```python
>>> goog.date = "6/11/2007"
>>> goog.__dict__
... observe la salida...
>>> ibm.__dict__
... observe la salida...
>>>
```

En la salida anterior, notará que la instancia `goog` tiene un atributo `date`, mientras que la instancia `ibm` no. Es importante destacar que Python realmente no impone ninguna restricción sobre los atributos. Por ejemplo, los atributos de una instancia no se limitan a los establecidos en el método `__init__()`.

En lugar de establecer un atributo, intente colocar un nuevo valor directamente en el objeto `__dict__`:

```python
>>> goog.__dict__['time'] = '9:45am'
>>> goog.time
'9:45am'
>>>
```

Aquí, realmente se nota el hecho de que una instancia es una capa sobre un diccionario.
