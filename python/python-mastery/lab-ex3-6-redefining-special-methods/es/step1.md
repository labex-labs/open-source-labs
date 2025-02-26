# Mejor salida para representar objetos

Todos los objetos de Python tienen dos representaciones en cadena. La primera representación se crea mediante la conversión a cadena a través de `str()` (que es llamada por `print`). La representación en cadena suele ser una versión bien formateada del objeto destinada a ser leída por humanos. La segunda representación es una representación de código del objeto creada por `repr()` (o simplemente al visualizar un valor en la shell interactiva). La representación de código suele mostrarte el código que tienes que escribir para obtener el objeto. Aquí hay un ejemplo que ilustra el uso de fechas:

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # utiliza str()
2008-07-05
>>> d    # utiliza repr()
datetime.date(2008, 7, 5)
>>>
```

Hay varias técnicas para obtener la cadena `repr()` en la salida:

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
>>>
```

Modifica el objeto `Stock` que has creado de modo que el método `__repr__()` produzca una salida más útil. Por ejemplo:

```python
>>> goog = Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

Ve lo que sucede cuando lees un portafolio de acciones y visualizas la lista resultante después de haber realizado estos cambios. Por ejemplo:

```python
>>> import stock, reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23),
 Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
>>>
```
