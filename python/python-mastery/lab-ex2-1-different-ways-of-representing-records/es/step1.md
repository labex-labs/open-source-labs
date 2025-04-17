# Explorando el Conjunto de Datos (Dataset)

Comencemos nuestro viaje echando un vistazo de cerca al conjunto de datos (dataset) con el que vamos a trabajar. El archivo `ctabus.csv` es un archivo CSV (Comma-Separated Values, valores separados por comas). Los archivos CSV son una forma común de almacenar datos tabulares, donde cada línea representa una fila, y los valores dentro de una fila están separados por comas. Este archivo en particular contiene datos diarios de pasajeros del sistema de autobuses de la Autoridad de Tránsito de Chicago (CTA, Chicago Transit Authority), que cubren el período del 1 de enero de 2001 al 31 de agosto de 2013.

Descomprime el archivo y elimina el archivo zip:

```bash
cd /home/labex/project
unzip ctabus.csv.zip
rm ctabus.csv.zip
```

Para comprender la estructura de este archivo, primero echaremos un vistazo dentro de él. Usaremos Python para leer el archivo e imprimir algunas líneas. Abre una terminal y ejecuta el siguiente código Python:

```python
f = open('/home/labex/project/ctabus.csv')
print(next(f))  # Read the header line
print(next(f))  # Read the first data line
print(next(f))  # Read the second data line
f.close()
```

En este código, primero abrimos el archivo usando la función `open` y lo asignamos a la variable `f`. La función `next` se utiliza para leer la siguiente línea del archivo. La usamos tres veces: la primera vez para leer la línea de encabezado (header), que generalmente contiene los nombres de las columnas en el conjunto de datos (dataset). La segunda y tercera vez, leemos la primera y segunda línea de datos respectivamente. Finalmente, cerramos el archivo usando el método `close` para liberar recursos del sistema.

Deberías ver una salida similar a esta:

```
route,date,daytype,rides

3,01/01/2001,U,7354

4,01/01/2001,U,9288
```

Esta salida muestra que el archivo tiene 4 columnas de datos. Desglosemos lo que representa cada columna:

1. `route`: Este es el nombre o número de la ruta del autobús. Es la primera columna (Columna 0) en el conjunto de datos (dataset).
2. `date`: Es una cadena de fecha (date string) en el formato MM/DD/AAAA. Esta es la segunda columna (Columna 1).
3. `daytype`: Es un código de tipo de día, que es la tercera columna (Columna 2).
   - U = Domingo/Festivo (Sunday/Holiday)
   - A = Sábado (Saturday)
   - W = Día de la semana (Weekday)
4. `rides`: Esta columna registra el número total de pasajeros como un entero. Es la cuarta columna (Columna 3).

La columna `rides` nos dice cuántas personas abordaron un autobús en una ruta específica en un día determinado. Por ejemplo, de la salida anterior, podemos ver que 7,354 personas viajaron en el autobús número 3 el 1 de enero de 2001.

Ahora, averigüemos cuántas líneas hay en el archivo. Conocer el número de líneas nos dará una idea del tamaño de nuestro conjunto de datos (dataset). Ejecuta el siguiente código Python:

```python
with open('/home/labex/project/ctabus.csv') as f:
    line_count = sum(1 for line in f)
    print(f"Total lines in the file: {line_count}")
```

En este código, usamos la declaración `with` para abrir el archivo. La ventaja de usar `with` es que se encarga automáticamente de cerrar el archivo cuando terminamos con él. Luego usamos una expresión generadora `(1 for line in f)` para crear una secuencia de 1s, uno por cada línea en el archivo. La función `sum` suma todos estos 1s, dándonos el número total de líneas en el archivo. Finalmente, imprimimos el resultado.

Esto debería generar aproximadamente 577,564 líneas, lo que significa que estamos lidiando con un conjunto de datos (dataset) sustancial. Este gran conjunto de datos (dataset) nos proporcionará muchos datos para analizar y extraer información.
