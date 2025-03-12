# Construcción de una tubería de datos más compleja

Ahora, llevaremos nuestra tubería de datos al siguiente nivel agregando filtrado y mejorando la presentación de los datos. Esto hará que sea más fácil analizar y entender la información con la que estamos trabajando. Realizaremos cambios en nuestro script `ticker.py`. Filtrar los datos nos ayudará a centrarnos en la información específica que nos interesa, y presentarla en una tabla bien formateada la hará más legible.

## Actualización del archivo ticker.py

1. Primero, abre tu archivo `ticker.py` en el WebIDE. El WebIDE es una herramienta que te permite escribir y editar código directamente en tu navegador. Proporciona un entorno conveniente para realizar cambios en tus scripts de Python.

2. A continuación, necesitamos reemplazar el bloque `if __name__ == '__main__':` en el archivo `ticker.py` con el siguiente código. Este bloque de código es el punto de entrada de nuestro script, y al reemplazarlo, estaremos cambiando cómo el script procesa y muestra los datos.

```python
if __name__ == '__main__':
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter('text')

    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name', 'price', 'change'], formatter)
```

3. Después de realizar estos cambios, guarda el archivo. Puedes hacerlo presionando `Ctrl+S` en tu teclado o seleccionando "File" → "Save" desde el menú. Guardar el archivo asegura que tus cambios se conserven y se puedan ejecutar más tarde.

## Comprensión de la tubería mejorada

Echemos un vistazo más detallado a lo que hace esta tubería mejorada. Comprender cada paso te ayudará a ver cómo las diferentes partes del código trabajan juntas para procesar y mostrar los datos.

1. Comenzamos importando `create_formatter` y `print_table` del módulo `tableformat`. Este módulo ya está configurado para ti y proporciona funciones que nos ayudan a formatear y mostrar los datos en una tabla agradable.

2. Luego, creamos un formateador de texto utilizando `create_formatter('text')`. Este formateador se utilizará para formatear los datos de una manera fácil de leer.

3. Ahora, desglosemos la tubería paso a paso:
   - `follow('stocklog.csv')` es una función que genera líneas del archivo `stocklog.csv`. Monitorea continuamente el archivo en busca de nuevos datos y proporciona las líneas una por una.
   - `csv.reader(lines)` toma las líneas generadas por `follow` y las analiza en datos de filas. Esto es necesario porque los datos en el archivo CSV están en formato de texto y necesitamos convertirlos en un formato estructurado con el que podamos trabajar.
   - `(Ticker.from_row(row) for row in rows)` es una expresión generadora que convierte cada fila de datos en un objeto `Ticker`. Un objeto `Ticker` representa una acción y contiene información como el nombre de la acción, el precio y el cambio.
   - `(rec for rec in records if rec.change < 0)` es otra expresión generadora que filtra los objetos `Ticker`. Solo conserva los objetos donde el cambio de precio de la acción es negativo. Esto nos permite centrarnos en las acciones que han disminuido de precio.
   - `print_table(negative, ['name', 'price', 'change'], formatter)` toma los objetos `Ticker` filtrados y los formatea en una tabla utilizando el formateador que creamos anteriormente. Luego, muestra la tabla en la consola.

Esta tubería demuestra el poder de los generadores. En lugar de cargar todos los datos del archivo en memoria a la vez, estamos encadenando múltiples operaciones (lectura, análisis, conversión, filtrado) y procesando los datos uno por uno. Esto ahorra memoria y hace que el código sea más eficiente.

## Ejecución de la tubería mejorada

Ejecutemos el código actualizado para ver los resultados.

1. Primero, asegúrate de que estás en el directorio del proyecto en la terminal. Si no estás allí, puedes navegar hasta él utilizando el siguiente comando:

   ```bash
   cd /home/labex/project
   ```

2. Una vez que estés en el directorio del proyecto, ejecuta el script `ticker.py` utilizando el siguiente comando:

   ```bash
   python3 ticker.py
   ```

3. Después de ejecutar el script, deberías ver una tabla bien formateada en la terminal. Esta tabla muestra solo las acciones con cambios de precio negativos.

   ```
          name      price     change
    ---------- ---------- ----------
             C      53.12      -0.21
           UTX      70.04      -0.19
           AXP      62.86      -0.18
           MMM      85.72      -0.22
           MCD      51.38      -0.03
           WMT      49.85      -0.23
            KO       51.6      -0.07
           AIG      71.39      -0.14
            PG      63.05      -0.02
            HD      37.76      -0.19
   ```

Si has visto suficiente salida y quieres detener la ejecución del script, puedes presionar `Ctrl+C` en tu teclado.

## El poder de las tuberías de generadores

Lo que hemos creado aquí es una poderosa tubería de procesamiento de datos. Resumamos lo que hace:

1. Monitorea continuamente el archivo `stocklog.csv` en busca de nuevos datos. Esto significa que a medida que se agreguen nuevos datos al archivo, la tubería los procesará automáticamente.
2. Analiza los datos CSV del archivo en objetos `Ticker` estructurados. Esto hace que sea más fácil trabajar con los datos y realizar operaciones en ellos.
3. Filtra los datos según un criterio específico, en este caso, cambios de precio negativos. Esto nos permite centrarnos en las acciones que están perdiendo valor.
4. Formatea y presenta los datos filtrados en una tabla legible. Esto hace que sea fácil analizar los datos y sacar conclusiones.

Una de las principales ventajas de usar generadores en esta tubería es que utiliza una cantidad mínima de memoria. Los generadores producen valores a demanda, lo que significa que no almacenan todos los datos en memoria a la vez. Esto es similar a las tuberías Unix, donde cada componente procesa los datos y los pasa al siguiente componente.

Puedes pensar en los generadores como bloques de Lego. Al igual que puedes apilar bloques de Lego para crear diferentes estructuras, puedes combinar generadores para crear flujos de trabajo de procesamiento de datos poderosos. Este enfoque modular te permite construir sistemas complejos a partir de componentes simples y reutilizables.
