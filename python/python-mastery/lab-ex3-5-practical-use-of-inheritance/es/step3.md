# Implementando un Formateador Concreto

Ahora que hemos definido nuestra clase base abstracta y actualizado la función `print_table()`, es hora de crear una clase de formateador concreto. Una clase de formateador concreto es aquella que proporciona implementaciones reales para los métodos definidos en la clase base abstracta. En nuestro caso, crearemos una clase que pueda formatear datos en una tabla de texto plano.

Agreguemos la siguiente clase a tu archivo `tableformat.py`. Esta clase heredará de la clase base abstracta `TableFormatter` e implementará los métodos `headings()` y `row()`.

```python
class TextTableFormatter(TableFormatter):
    """
    Formatter that generates a plain - text table.
    """
    def headings(self, headers):
        """
        Generate plain - text table headings.
        """
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        """
        Generate a plain - text table row.
        """
        print(' '.join('%10s' % d for d in rowdata))
```

La clase `TextTableFormatter` hereda de `TableFormatter`. Esto significa que obtiene todas las propiedades y métodos de la clase `TableFormatter`, pero también proporciona sus propias implementaciones para los métodos `headings()` y `row()`. Estos métodos son responsables de formatear los encabezados y las filas de la tabla respectivamente. El método `headings()` imprime los encabezados de una manera bien formateada, seguido de una línea de guiones para separar los encabezados de los datos. El método `row()` formatea cada fila de datos de manera similar.

Ahora, probemos nuestro nuevo formateador. Utilizaremos los módulos `stock`, `reader` y `tableformat` para leer datos de un archivo CSV e imprimirlos utilizando nuestro nuevo formateador.

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TextTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Cuando ejecutes este código, deberías ver la misma salida que antes. Esto se debe a que nuestro nuevo formateador está diseñado para producir la misma tabla de texto plano que la función original `print_table()`.

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Esta salida confirma que nuestro `TextTableFormatter` está funcionando correctamente. La ventaja de utilizar este enfoque es que hemos hecho nuestro código más modular y extensible. Al separar la lógica de formateo en una jerarquía de clases separada, podemos agregar fácilmente nuevos formatos de salida. Todo lo que necesitamos hacer es crear nuevas subclases de `TableFormatter` sin modificar la función `print_table()`. De esta manera, podremos admitir diferentes formatos de salida como CSV o HTML en el futuro.
