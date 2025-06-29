# Creación de la clase Ticker

En el procesamiento de datos, trabajar con datos sin procesar puede ser bastante desafiante. Para que nuestro trabajo con los datos de acciones sea más organizado y eficiente, definiremos una clase adecuada para representar las cotizaciones de acciones. Esta clase servirá como un modelo para nuestros datos de acciones, lo que hará que nuestra tubería de procesamiento de datos sea más robusta y fácil de administrar.

## Creación del archivo ticker.py

1. Primero, necesitamos crear un nuevo archivo en el WebIDE. Puedes hacerlo haciendo clic en el icono "New File" o haciendo clic derecho en el explorador de archivos y seleccionando "New File". Nombrar este archivo `ticker.py`. Este archivo contendrá el código de nuestra clase `Ticker`.

2. Ahora, agreguemos el siguiente código al archivo `ticker.py` recién creado. Este código definirá nuestra clase `Ticker` y configurará una simple tubería de procesamiento para probarla.

```python
# ticker.py

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

if __name__ == '__main__':
    from follow import follow
    import csv
    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    for record in records:
        print(record)
```

3. Después de agregar el código, guarda el archivo. Puedes hacerlo presionando `Ctrl+S` o seleccionando "File" → "Save" desde el menú. Guardar el archivo asegura que tus cambios se conserven y se puedan ejecutar más tarde.

## Comprensión del código

Echemos un vistazo más detallado a lo que hace este código paso a paso:

1. Al principio del código, estamos importando `Structure` y tipos de campos del módulo `structure.py`. Este módulo ya se ha configurado para ti. Estas importaciones son esenciales porque proporcionan los bloques de construcción para nuestra clase `Ticker`. La clase `Structure` será la clase base para nuestra clase `Ticker`, y los tipos de campos como `String`, `Float` e `Integer` definirán los tipos de datos de nuestros campos de datos de acciones.

2. A continuación, definimos una clase `Ticker` que hereda de `Structure`. Esta clase tiene varios campos que representan diferentes aspectos de los datos de acciones:
   - `name`: Este campo almacena el símbolo de la acción, como "IBM" o "AAPL". Nos ayuda a identificar de qué empresa es la acción con la que estamos trabajando.
   - `price`: Contiene el precio actual de la acción. Esta es una información crucial para los inversionistas.
   - `date` y `time`: Estos campos nos indican cuándo se generó la cotización de la acción. Saber la hora y la fecha es importante para analizar las tendencias de precios de las acciones a lo largo del tiempo.
   - `change`: Esto representa el cambio de precio de la acción. Muestra si el precio de la acción ha subido o bajado en comparación con un punto anterior.
   - `open`, `high`, `low`: Estos campos representan el precio de apertura, el precio más alto y el precio más bajo de la acción durante un cierto período. Nos dan una idea del rango de precios de la acción.
   - `volume`: Este campo almacena el número de acciones negociadas. Un alto volumen de negociación puede indicar un fuerte interés del mercado en una acción en particular.

3. En el bloque `if __name__ == '__main__':`, configuramos una tubería de procesamiento. Este bloque de código se ejecutará cuando ejecutemos directamente el archivo `ticker.py`.
   - `follow('stocklog.csv')` es una función que genera líneas del archivo `stocklog.csv`. Nos permite leer el archivo línea por línea.
   - `csv.reader(lines)` toma estas líneas y las analiza en datos de filas. CSV (Comma - Separated Values) es un formato de archivo común para almacenar datos tabulares, y esta función nos ayuda a extraer los datos de cada fila.
   - `(Ticker.from_row(row) for row in rows)` es una expresión generadora. Toma cada fila de datos y la convierte en un objeto `Ticker`. De esta manera, transformamos los datos CSV sin procesar en objetos estructurados que son más fáciles de manejar.
   - El bucle `for` itera sobre estos objetos `Ticker` y los imprime uno por uno. Esto nos permite ver los datos estructurados en acción.

## Ejecución del código

Ejecutemos el código para ver cómo funciona:

1. Primero, debemos asegurarnos de que estamos en el directorio del proyecto en la terminal. Si no estás allí, utiliza el siguiente comando para navegar hasta él:

   ```bash
   cd /home/labex/project
   ```

2. Una vez que estés en el directorio correcto, ejecuta el script `ticker.py` utilizando el siguiente comando:

   ```bash
   python3 ticker.py
   ```

3. Después de ejecutar el script, deberías ver una salida similar a esta (tus datos variarán):
   ```
   Ticker(IBM, 103.53, 6/11/2007, 09:53.59, 0.46, 102.87, 103.53, 102.77, 541633)
   Ticker(MSFT, 30.21, 6/11/2007, 09:54.01, 0.16, 30.05, 30.21, 29.95, 7562516)
   Ticker(AA, 40.01, 6/11/2007, 09:54.01, 0.35, 39.67, 40.15, 39.31, 576619)
   Ticker(T, 40.1, 6/11/2007, 09:54.08, -0.16, 40.2, 40.19, 39.87, 1312959)
   ```

Puedes detener la ejecución del script presionando `Ctrl+C` cuando hayas visto suficiente salida.

Observa cómo los datos CSV sin procesar se han transformado en objetos `Ticker` estructurados. Esta transformación hace que los datos sean mucho más fáciles de manejar en nuestra tubería de procesamiento, ya que ahora podemos acceder y manipular los datos de acciones utilizando los campos definidos en la clase `Ticker`.
