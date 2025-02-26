# Haciéndolo razonable

El uso de mixins puede ser una herramienta útil para los constructores de marcos para reducir la cantidad de código que se necesita escribir. Sin embargo, obligar a los usuarios a recordar cómo componer adecuadamente las clases y usar la herencia múltiple puede confundirlos. En el Ejercicio 3.5, escribió una función `create_formatter()` que facilitó la creación de un formateador personalizado. Tome esa función y extiéndala para entender algunos argumentos opcionales relacionados con las clases mixin. Por ejemplo:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('csv', column_formats=['"%s"','%d','%0.2f'])
>>> print_table(portfolio, ['name','shares','price'], formatter)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44

>>> formatter = create_formatter('text', upper_headers=True)
>>> print_table(portfolio, ['name','shares','price'], formatter)
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

En el fondo, la función `create_formatter()` compondrá adecuadamente las clases y devolverá una instancia correcta de `TableFormatter`.
