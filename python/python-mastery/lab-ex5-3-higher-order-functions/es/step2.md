# Creando una función de orden superior

En Python, una función de orden superior es una función que puede tomar otra función como argumento. Esto permite una mayor flexibilidad y reutilización de código. Ahora, vamos a crear una función de orden superior llamada `convert_csv()`. Esta función manejará las operaciones comunes de procesamiento de datos CSV, mientras te permite personalizar cómo se convierte cada fila del CSV en un registro.

Abre el archivo `reader.py` en el WebIDE. Vamos a agregar una función que tomará un iterable de datos CSV, una función de conversión y, opcionalmente, encabezados de columna. La función de conversión se utilizará para transformar cada fila del CSV en un registro.

Aquí está el código de la función `convert_csv()`. Cópialo y pégalo en tu archivo `reader.py`:

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function

    Args:
        lines: An iterable containing CSV data
        conversion_func: A function that takes headers and a row and returns a record
        headers: Column headers (optional). If None, the first row is used as headers

    Returns:
        A list of records as processed by conversion_func
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = conversion_func(headers, row)
        records.append(record)
    return records
```

Analicemos lo que hace esta función. Primero, inicializa una lista vacía llamada `records` para almacenar los registros convertidos. Luego, utiliza la función `csv.reader()` para leer las líneas de datos CSV. Si no se proporcionan encabezados, toma la primera fila como encabezados. Para cada fila subsiguiente, aplica la `conversion_func` para convertir la fila en un registro y lo agrega a la lista `records`. Finalmente, devuelve la lista de registros.

Ahora, necesitamos una función de conversión simple para probar nuestra función `convert_csv()`. Esta función tomará los encabezados y una fila y convertirá la fila en un diccionario utilizando los encabezados como claves.

Aquí está el código de la función `make_dict()`. Agrega esta función también a tu archivo `reader.py`:

```python
def make_dict(headers, row):
    '''
    Convert a row to a dictionary using the provided headers
    '''
    return dict(zip(headers, row))
```

La función `make_dict()` utiliza la función `zip()` para emparejar cada encabezado con su valor correspondiente en la fila y luego crea un diccionario a partir de estos pares.

Vamos a probar estas funciones. Abre una shell de Python ejecutando los siguientes comandos en la terminal:

```bash
cd ~/project
python3 -i reader.py
```

La opción `-i` en el comando `python3` inicia el intérprete de Python en modo interactivo e importa el archivo `reader.py`, para que podamos usar las funciones que acabamos de definir.

En la shell de Python, ejecuta el siguiente código para probar nuestras funciones:

```python
# Open the CSV file
lines = open('portfolio.csv')

# Convert to a list of dictionaries using our new function
result = convert_csv(lines, make_dict)

# Print the result
print(result)
```

Este código abre el archivo `portfolio.csv`, utiliza la función `convert_csv()` con la función de conversión `make_dict()` para convertir los datos CSV en una lista de diccionarios y luego imprime el resultado.

Deberías ver una salida similar a la siguiente:

```
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

Esta salida muestra que nuestra función de orden superior `convert_csv()` funciona correctamente. Hemos creado con éxito una función que toma otra función como argumento, lo que nos da la capacidad de cambiar fácilmente cómo se convierten los datos CSV.

Para salir de la shell de Python, puedes escribir `exit()` o presionar Ctrl+D.
