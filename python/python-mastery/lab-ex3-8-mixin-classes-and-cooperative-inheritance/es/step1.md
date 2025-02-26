# El problema con el formato de columnas

Si se regresa al Ejercicio 3.1, escribió una función `print_portfolio()` que producía una tabla como esta:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> print_portfolio(portfolio)
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

La función `print_table()` desarrollada en los últimos ejercicios casi reemplaza esta funcionalidad, casi. El único problema que tiene es que no puede formatear precisamente el contenido de cada columna. Por ejemplo, observe cómo los valores de la columna `price` se formatean precisamente con 2 decimales. La clase `TableFormatter` y las subclases relacionadas no pueden hacer eso.

Una forma de solucionarlo sería modificar la función `print_table()` para aceptar un argumento adicional de formatos. Por ejemplo, tal vez algo como esto:

```python
>>> def print_table(records, fields, formats, formatter):
        formatter.headings(fields)
        for r in records:
            rowdata = [(fmt % getattr(r, fieldname))
                 for fieldname,fmt in zip(fields,formats)]
            formatter.row(rowdata)

>>> import stock, reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> from tableformat import TextTableFormatter
>>> formatter = TextTableFormatter()
>>> print_table(portfolio,
                ['name','shares','price'],
                ['%s','%d','%0.2f'],
                formatter)

      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

Sí, se podría modificar `print_table()` de esta manera, pero ¿es ese el lugar adecuado para hacerlo? La idea general de todas las clases `TableFormatter` es que podrían usarse en diferentes tipos de aplicaciones. El formato de columnas es algo que podría ser útil en otros lugares, no solo en la función `print_table()`.

Otra posible aproximación podría ser cambiar la interfaz de la clase `TableFormatter` de alguna manera. Por ejemplo, tal vez agregando un tercer método para aplicar el formato.

```python
class TableFormatter:
    def headings(self, headers):
     ...
    def format(self, rowdata):
     ...
    def row(self, rowdata):
     ...
```

El problema aquí es que cada vez que se cambia la interfaz de una clase, se tendrá que refactorizar todo el código existente para que funcione con ella. Específicamente, tendría que modificar todas las subclases `TableFormatter` ya escritas y todo el código escrito para usarlas. No hagamos eso.

Como alternativa, un usuario podría usar la herencia para personalizar un formateador específico con el fin de inyectar algún formato en él. Por ejemplo, pruebe este experimento:

```python
>>> from tableformat import TextTableFormatter, print_table
>>> class PortfolioFormatter(TextTableFormatter):
        def row(self, rowdata):
            formats = ['%s','%d','%0.2f']
            rowdata = [(fmt % d) for fmt, d in zip(formats, rowdata)]
            super().row(rowdata)

>>> formatter = PortfolioFormatter()
>>> print_table(portfolio, ['name','shares','price'], formatter)
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

Sí, eso funciona, pero también es un poco torpe y extraño. El usuario tiene que elegir un formateador específico para personalizar. Además, tiene que implementar el código real de formato de columnas por sí mismo. Seguramente hay una forma diferente de hacer esto.
