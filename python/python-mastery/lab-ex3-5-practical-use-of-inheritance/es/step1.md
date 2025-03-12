# Comprendiendo el Problema

En este laboratorio, vamos a aprender sobre la herencia en Python y cómo puede ayudarnos a crear código que sea tanto extensible como adaptable. La herencia es un concepto poderoso en la programación orientada a objetos (object - oriented programming) donde una clase puede heredar atributos y métodos de otra clase. Esto nos permite reutilizar código y construir funcionalidades más complejas sobre el código existente.

Comencemos por observar la función existente `print_table()`. Esta es la función que mejoraremos para que sea más flexible en términos de formatos de salida.

Primero, debes abrir el archivo `tableformat.py` en el editor del WebIDE. La ruta a este archivo es la siguiente:

```
/home/labex/project/tableformat.py
```

Una vez que abras el archivo, verás la implementación actual de la función `print_table()`. Esta función está diseñada para formatear e imprimir datos tabulares. Toma dos entradas principales: una lista de registros (que son objetos) y una lista de nombres de campos. Basándose en estas entradas, imprime una tabla bien formateada.

Ahora, probemos esta función para ver cómo funciona. Abre una terminal en el WebIDE y ejecuta los siguientes comandos de Python. Estos comandos importan los módulos necesarios, leen datos de un archivo CSV y luego utilizan la función `print_table()` para mostrar los datos.

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

Después de ejecutar estos comandos, deberías ver la siguiente salida:

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

La salida se ve bien, pero esta función tiene una limitación. Actualmente, solo admite un formato de salida, que es texto plano. En escenarios del mundo real, es posible que desees mostrar tus datos en diferentes formatos como CSV, HTML u otros.

En lugar de hacer cambios en la función `print_table()` cada vez que queramos admitir un nuevo formato de salida, podemos utilizar la herencia para crear una solución más flexible. Así es como lo haremos:

1. Definiremos una clase base `TableFormatter`. Esta clase tendrá métodos que se utilizarán para formatear datos. La clase base proporciona una estructura y funcionalidad comunes sobre las cuales todas las subclases pueden construir.
2. Crearemos varias subclases. Cada subclase estará diseñada para un formato de salida diferente. Por ejemplo, una subclase podría ser para la salida en formato CSV, otra para la salida en formato HTML, y así sucesivamente. Estas subclases heredarán los métodos de la clase base y también pueden agregar su propia funcionalidad específica.
3. Modificaremos la función `print_table()` para que pueda trabajar con cualquier formateador. Esto significa que podemos pasar diferentes subclases de la clase `TableFormatter` a la función `print_table()`, y esta será capaz de utilizar los métodos de formato adecuados.

Este enfoque tiene una gran ventaja. Nos permite agregar nuevos formatos de salida sin cambiar la funcionalidad central de la función `print_table()`. Entonces, a medida que cambien tus requisitos y necesites admitir más formatos de salida, puedes hacerlo fácilmente creando nuevas subclases.
