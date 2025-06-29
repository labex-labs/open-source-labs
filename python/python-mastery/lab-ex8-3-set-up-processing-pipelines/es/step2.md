# Creación de componentes de tubería de corrutinas

En este paso, vamos a crear corrutinas más especializadas para procesar datos de acciones. Una corrutina es un tipo especial de función que puede pausar y reanudar su ejecución, lo cual es muy útil para construir tuberías de procesamiento de datos. Cada corrutina que creemos realizará una tarea específica en nuestra tubería de procesamiento general.

1. Primero, necesitas crear un nuevo archivo. Navega hasta el directorio `/home/labex/project` y crea un archivo llamado `coticker.py`. Este archivo contendrá todo el código para nuestro procesamiento de datos basado en corrutinas.

2. Ahora, comencemos a escribir código en el archivo `coticker.py`. Primero importaremos los módulos necesarios y definiremos la estructura básica. Los módulos son bibliotecas de código preescritas que proporcionan funciones y clases útiles. El siguiente código hace precisamente eso:

```python
# coticker.py
from structure import Structure

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

3. Cuando mires el código anterior, notarás que hay errores relacionados con `String()`, `Float()` e `Integer()`. Estas son clases que necesitamos importar. Entonces, agregaremos las importaciones necesarias en la parte superior del archivo. De esta manera, Python sabe dónde encontrar estas clases. Aquí está el código actualizado:

```python
# coticker.py
from structure import Structure, String, Float, Integer

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

4. A continuación, agregaremos los componentes de corrutina que formarán nuestra tubería de procesamiento de datos. Cada corrutina tiene un trabajo específico en la tubería. Aquí está el código para agregar estas corrutinas:

```python
@consumer
def to_csv(target):
    def producer():
        while True:
            line = yield

    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)
```

5. Comprendamos lo que hace cada una de estas corrutinas:
   - `to_csv`: Su trabajo es convertir líneas de texto sin procesar en filas CSV analizadas. Esto es importante porque nuestros datos inicialmente están en formato de texto y necesitamos dividirlos en datos CSV estructurados.
   - `create_ticker`: Esta corrutina toma las filas CSV y crea objetos `Ticker` a partir de ellas. Los objetos `Ticker` representan los datos de acciones de una manera más organizada.
   - `negchange`: Filtra los objetos `Ticker`. Solo pasa las acciones que tienen cambios de precio negativos. Esto nos ayuda a centrarnos en las acciones que están perdiendo valor.
   - `ticker`: Esta corrutina formatea y muestra los datos de cotización. Utiliza un formateador para presentar los datos en una tabla agradable y legible.

6. Finalmente, necesitamos agregar el código del programa principal que conecta todos estos componentes. Este código configurará el flujo de datos a través de la tubería. Aquí está el código:

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change']

    # Create the processing pipeline
    t = ticker('text', fields)
    neg_filter = negchange(t)
    tick_creator = create_ticker(neg_filter)
    csv_parser = to_csv(tick_creator)

    # Connect the pipeline to the data source
    follow('stocklog.csv', csv_parser)
```

7. Después de escribir todo el código, guarda el archivo `coticker.py`. Luego, abre la terminal y ejecuta los siguientes comandos. El comando `cd` cambia el directorio al lugar donde se encuentra nuestro archivo, y el comando `python3` ejecuta nuestro script de Python:

```bash
cd /home/labex/project
python3 coticker.py
```

8. Si todo sale bien, deberías ver una tabla formateada en la terminal. Esta tabla muestra las acciones con cambios de precio negativos. La salida se verá algo así:

```
      name      price     change
---------- ---------- ----------
      MSFT      72.50      -0.25
        AA      35.25      -0.15
       IBM      50.10      -0.15
      GOOG     100.02      -0.01
      AAPL     102.50      -0.06
```

Ten en cuenta que los valores reales en la tabla pueden variar dependiendo de los datos de acciones generados.

## Comprender el flujo de la tubería

La parte más importante de este programa es cómo fluyen los datos a través de las corrutinas. Analicémoslo paso a paso:

1. La función `follow` comienza leyendo líneas del archivo `stocklog.csv`. Este es nuestro origen de datos.
2. Cada línea que se lee se envía luego a la corrutina `csv_parser`. El `csv_parser` toma la línea de texto sin procesar y la analiza en campos CSV.
3. Los datos CSV analizados se envían luego a la corrutina `tick_creator`. Esta corrutina crea objetos `Ticker` a partir de las filas CSV.
4. Los objetos `Ticker` se envían luego a la corrutina `neg_filter`. Esta corrutina comprueba cada objeto `Ticker`. Si la acción tiene un cambio de precio negativo, pasa el objeto; de lo contrario, lo descarta.
5. Finalmente, los objetos `Ticker` filtrados se envían a la corrutina `ticker`. La corrutina `ticker` formatea los datos y los muestra en una tabla.

Esta arquitectura de tubería es muy útil porque permite que cada componente se centre en una sola tarea. Esto hace que el código sea más modular, lo que significa que es más fácil de entender, modificar y mantener.
