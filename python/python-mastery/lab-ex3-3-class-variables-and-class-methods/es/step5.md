# Generalizando

Una característica útil de los métodos de clase es que se pueden usar para poner una interfaz de creación de instancias altamente uniforme en una amplia variedad de clases y escribir funciones de utilidad general que las usen.

Antes, creaste un archivo `reader.py` que tenía algunas funciones para leer datos CSV. Agrega la siguiente función `read_csv_as_instances()` al archivo que acepta una clase como entrada y usa el método `from_row()` de la clase para crear una lista de instancias:

```python
# reader.py
...

def read_csv_as_instances(filename, cls):
    '''
    Lee un archivo CSV en una lista de instancias
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

Elimina la función `read_portfolio()`: ya no la necesitas. Si quieres leer una lista de objetos `Stock`, haz lo siguiente:

```python
>>> # Lee un portafolio de instancias de Stock
>>> from reader import read_csv_as_instances
>>> from stock import Stock
>>> portfolio = read_csv_as_instances('portfolio.csv', Stock)
>>> portfolio
[<__main__.Stock object at 0x100674748>,
<__main__.Stock object at 0x1006746d8>,
<__main__.Stock object at 0x1006747b8>,
<__main__.Stock object at 0x100674828>,
<__main__.Stock object at 0x100674898>,
<__main__.Stock object at 0x100674908>,
<__main__.Stock object at 0x100674978>]
>>>
```

Aquí hay otro ejemplo de cómo podrías usar `read_csv_as_instances()` con una clase completamente diferente:

```python
>>> class Row:
         def __init__(self, route, date, daytype, numrides):
             self.route = route
             self.date = date
             self.daytype = daytype
             self.numrides = numrides
         @classmethod
         def from_row(cls, row):
             return cls(row[0], row[1], row[2], int(row[3]))

>>> rides = read_csv_as_instances('ctabus.csv', Row)
>>> len(rides)
577563
>>>
```

**Discusión**

Este laboratorio ilustra los dos usos más comunes de las variables de clase y los métodos de clase. Las variables de clase a menudo se usan para almacenar un parámetro global (por ejemplo, una configuración) que se comparte entre todas las instancias. A veces, las subclases heredarán de la clase base y sobrescribirán la configuración para cambiar el comportamiento.

Los métodos de clase se usan más comúnmente para implementar constructores alternativos como se muestra. Una forma común de detectar estos métodos de clase es buscar la palabra "from" en el nombre. Por ejemplo, aquí hay un ejemplo en los diccionarios integrados:

```python
>>> d = dict.fromkeys(['a','b','c'], 0)     # método de clase
>>> d
{'a': 0, 'c': 0, 'b': 0}
>>>
```
