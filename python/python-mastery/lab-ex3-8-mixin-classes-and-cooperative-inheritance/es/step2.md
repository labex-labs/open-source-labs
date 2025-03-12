# Implementando clases mixin para formateo

En este paso, vamos a aprender sobre las clases mixin. Las clases mixin son una técnica realmente útil en Python. Permiten agregar funcionalidad adicional a las clases sin cambiar su código original. Esto es genial porque ayuda a mantener el código modular y fácil de gestionar.

## ¿Qué son las clases mixin?

Una clase mixin es un tipo especial de clase. Su propósito principal es proporcionar cierta funcionalidad que puede ser heredada por otra clase. Sin embargo, una clase mixin no está destinada a ser utilizada por sí misma. No se crea una instancia de una clase mixin directamente. En lugar de eso, se utiliza como una forma de agregar características específicas a otras clases de manera controlada y predecible. Esto es una forma de herencia múltiple, donde una clase puede heredar de más de una clase padre.

Ahora, implementemos dos clases mixin en nuestro archivo `tableformat.py`. Primero, abre el archivo en el editor. Puedes hacer esto ejecutando los siguientes comandos en la terminal:

```bash
cd ~/project
code tableformat.py
```

Una vez abierto el archivo, agrega las siguientes definiciones de clase al final del archivo, pero antes de cualquier función existente.

```python
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
```

Esta clase `ColumnFormatMixin` proporciona funcionalidad de formateo de columnas. La variable de clase `formats` es una lista que contiene códigos de formato. Estos códigos se utilizan para formatear los datos de cada columna. El método `row()` toma los datos de la fila, aplica los códigos de formato a cada elemento de la fila y luego pasa los datos de la fila formateados a la clase padre utilizando `super().row(rowdata)`.

A continuación, agrega otra clase mixin que hace que los encabezados de la tabla aparezcan en mayúsculas:

```python
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
```

Esta clase `UpperHeadersMixin` transforma el texto de los encabezados a mayúsculas. Toma la lista de encabezados, convierte cada encabezado a mayúsculas y luego pasa los encabezados modificados al método `headings()` de la clase padre utilizando `super().headings()`.

## Utilizando las clases mixin

Probemos nuestras nuevas clases mixin. Ejecutaremos algún código de Python para ver cómo funcionan.

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Cuando ejecutes este código, deberías ver una salida bien formateada. La columna de precio tendrá una cantidad consistente de decimales gracias al formateo proporcionado por la clase `ColumnFormatMixin`.

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Ahora, probemos la clase `UpperHeadersMixin`. Ejecuta el siguiente código:

```python
python3 -c "
from tableformat import TextTableFormatter, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
    pass

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Este código debería mostrar los encabezados en mayúsculas.

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

## Entendiendo la herencia cooperativa

Fíjate que en nuestras clases mixin, utilizamos `super().method()`. Esto se llama "herencia cooperativa". En la herencia cooperativa, cada clase en la cadena de herencia trabaja en conjunto. Cuando una clase llama a `super().method()`, está pidiendo a la siguiente clase en la cadena que realice su parte de la tarea. De esta manera, una cadena de clases puede agregar su propio comportamiento al proceso general.

El orden de herencia es muy importante. Cuando definimos `class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter)`, Python busca los métodos primero en `ColumnFormatMixin` y luego en `TextTableFormatter`. Entonces, cuando se llama a `super().row()` en la clase `ColumnFormatMixin`, se refiere a `TextTableFormatter.row()`.

Incluso podemos combinar ambas clases mixin. Ejecuta el siguiente código:

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, UpperHeadersMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Este código nos dará tanto encabezados en mayúsculas como números formateados.

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

En el siguiente paso, haremos que estas clases mixin sean más fáciles de usar mejorando la función `create_formatter()`.
