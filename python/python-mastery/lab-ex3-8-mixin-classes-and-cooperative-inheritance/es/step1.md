# Comprendiendo el problema con el formato de columnas

En este paso, vamos a analizar una limitación en nuestra implementación actual de formato de tablas. También examinaremos algunas posibles soluciones a este problema.

Primero, entendamos qué vamos a hacer. Abriremos el editor VSCode y revisaremos el archivo `tableformat.py` en el directorio del proyecto. Este archivo es importante porque contiene el código que nos permite formatear datos tabulares de diferentes maneras, como en formato de texto, CSV o HTML.

Para abrir el archivo, usaremos los siguientes comandos en la terminal. El comando `cd` cambia el directorio al directorio del proyecto, y el comando `code` abre el archivo `tableformat.py` en VSCode.

```bash
cd ~/project
code tableformat.py
```

Cuando abras el archivo, notarás que hay varias clases definidas. Estas clases desempeñan diferentes roles en el formato de los datos de la tabla.

- `TableFormatter`: Esta es una clase base abstracta. Tiene métodos que se utilizan para formatear los encabezados y las filas de la tabla. Piénsala como un modelo para otras clases de formateadores.
- `TextTableFormatter`: Esta clase se utiliza para mostrar la tabla en formato de texto plano.
- `CSVTableFormatter`: Es responsable de formatear los datos de la tabla en formato CSV (Valores Separados por Comas).
- `HTMLTableFormatter`: Esta clase formatea los datos de la tabla en formato HTML.

También hay una función `print_table()` en el archivo. Esta función utiliza las clases de formateadores que acabamos de mencionar para mostrar los datos tabulares.

Ahora, veamos cómo funcionan estas clases ejecutando algún código de Python. Abre una terminal y inicia una sesión de Python. El siguiente código importa las funciones y clases necesarias del archivo `tableformat.py`, crea un objeto `TextTableFormatter` y luego utiliza la función `print_table()` para mostrar los datos de la cartera.

```python
python3 -c "
from tableformat import print_table, TextTableFormatter, portfolio
formatter = TextTableFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Después de ejecutar el código, deberías ver una salida similar a esta:

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

Ahora, encontremos el problema. Fíjate que los valores en la columna `price` no están formateados de manera consistente. Algunos valores tienen un decimal, como 32.2, mientras que otros tienen dos decimales, como 51.23. En datos financieros, generalmente queremos que el formato sea consistente.

Así es como queremos que se vea la salida:

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

Una forma de solucionar esto es modificar la función `print_table()` para que acepte especificaciones de formato. El siguiente código muestra cómo podemos hacer esto. Definimos una nueva función `print_table()` que toma un parámetro adicional `formats`. Dentro de la función, usamos estas especificaciones de formato para formatear cada valor en la fila.

```python
python3 -c "
from tableformat import TextTableFormatter, portfolio

def print_table(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [(fmt % getattr(r, fieldname))
             for fieldname, fmt in zip(fields, formats)]
        formatter.row(rowdata)

formatter = TextTableFormatter()
print_table(portfolio,
            ['name','shares','price'],
            ['%s','%d','%0.2f'],
            formatter)
"
```

Esta solución funciona, pero tiene una desventaja. Cambiar la interfaz de la función podría romper el código existente que utiliza la versión antigua de la función `print_table()`.

Otro enfoque es crear un formateador personalizado mediante la creación de una subclase. Podemos crear una nueva clase que herede de `TextTableFormatter` y sobrescribir el método `row()` para aplicar el formato deseado.

```python
python3 -c "
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        formats = ['%s','%d','%0.2f']
        rowdata = [(fmt % d) for fmt, d in zip(formats, rowdata)]
        super().row(rowdata)

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Esta solución también funciona, pero no es muy conveniente. Cada vez que queremos un formato diferente, tenemos que crear una nueva clase. Y estamos limitados al tipo de formateador específico del que estamos creando una subclase, en este caso, `TextTableFormatter`.

En el siguiente paso, exploraremos una solución más elegante utilizando clases mixin.
