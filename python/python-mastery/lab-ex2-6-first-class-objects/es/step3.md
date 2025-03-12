# Explorando el Modelo de Memoria de Python

El modelo de memoria de Python juega un papel crucial en la determinación de cómo se almacenan los objetos en memoria y cómo se les hace referencia. Comprender este modelo es esencial, especialmente cuando se trabaja con grandes conjuntos de datos, ya que puede afectar significativamente el rendimiento y el uso de memoria de tus programas en Python. En este paso, nos centraremos específicamente en cómo se manejan los objetos de cadena en Python y exploraremos formas de optimizar el uso de memoria para grandes conjuntos de datos.

## Repetición de Cadenas en Conjuntos de Datos

Los datos de autobuses del CTA contienen muchos valores repetidos, como los nombres de las rutas. Los valores repetidos en un conjunto de datos pueden provocar un uso ineficiente de la memoria si no se manejan adecuadamente. Para entender la magnitud de este problema, primero examinemos cuántas cadenas de ruta únicas hay en el conjunto de datos.

Primero, abre un intérprete de Python. Puedes hacer esto ejecutando el siguiente comando en tu terminal:

```bash
python3
```

Una vez que el intérprete de Python esté abierto, cargaremos los datos de autobuses del CTA y encontraremos las rutas únicas. Aquí está el código para lograr esto:

```python
import reader
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])

# Find unique route names
routes = {row['route'] for row in rows}
print(f"Number of unique route names: {len(routes)}")
```

En este código, primero importamos el módulo `reader`, que presumiblemente contiene una función para leer archivos CSV como diccionarios. Luego usamos la función `read_csv_as_dicts` para cargar los datos del archivo `ctabus.csv`. El segundo argumento `[str, str, str, int]` especifica los tipos de datos para cada columna en el archivo CSV. Después de eso, usamos una comprensión de conjunto para encontrar todos los nombres de ruta únicos en el conjunto de datos y mostramos la cantidad de nombres de ruta únicos.

La salida debería ser:

```
Number of unique route names: 181
```

Ahora, veamos cuántos objetos de cadena diferentes se crean para estas rutas. Aunque solo hay 181 nombres de ruta únicos, Python podría crear un nuevo objeto de cadena para cada aparición de un nombre de ruta en el conjunto de datos. Para verificar esto, usaremos la función `id()` para obtener el identificador único de cada objeto de cadena.

```python
# Count unique string object IDs
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects: {len(routeids)}")
```

La salida puede sorprenderte:

```
Number of unique route string objects: 542305
```

Esto muestra que solo hay 181 nombres de ruta únicos, pero más de 500,000 objetos de cadena únicos. Esto sucede porque Python crea un nuevo objeto de cadena para cada fila, incluso si los valores son los mismos. Esto puede provocar un desperdicio significativo de memoria, especialmente cuando se trabaja con grandes conjuntos de datos.

## Internamiento de Cadenas para Ahorrar Memoria

Python proporciona una forma de "internar" (reutilizar) cadenas utilizando la función `sys.intern()`. El internamiento de cadenas puede ahorrar memoria cuando tienes muchas cadenas duplicadas en tu conjunto de datos. Cuando internas una cadena, Python comprueba si una cadena idéntica ya existe en el grupo de cadenas internadas. Si es así, devuelve una referencia al objeto de cadena existente en lugar de crear uno nuevo.

Demostremos cómo funciona el internamiento de cadenas con un ejemplo sencillo:

```python
import sys

# Without interning
a = 'hello world'
b = 'hello world'
print(f"a is b (without interning): {a is b}")

# With interning
a = sys.intern(a)
b = sys.intern(b)
print(f"a is b (with interning): {a is b}")
```

En este código, primero creamos dos variables de cadena `a` y `b` con el mismo valor sin internamiento. El operador `is` comprueba si dos variables se refieren al mismo objeto. Sin internamiento, `a` y `b` son objetos diferentes, por lo que `a is b` devuelve `False`. Luego, internamos ambas cadenas utilizando `sys.intern()`. Después del internamiento, `a` y `b` se refieren al mismo objeto en el grupo de cadenas internadas, por lo que `a is b` devuelve `True`.

La salida debería ser:

```
a is b (without interning): False
a is b (with interning): True
```

Ahora, usemos el internamiento de cadenas al leer los datos de autobuses del CTA para reducir el uso de memoria. También usaremos el módulo `tracemalloc` para seguir el uso de memoria antes y después del internamiento.

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for the route column
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, str, str, int])

# Check unique route objects again
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects (with interning): {len(routeids)}")

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

En este código, primero comenzamos a seguir el uso de memoria utilizando `tracemalloc.start()`. Luego, leemos los datos de autobuses del CTA con internamiento para la columna de ruta pasando `sys.intern` como el tipo de datos para la primera columna. Después de eso, comprobamos la cantidad de objetos de cadena de ruta únicos nuevamente y mostramos el uso de memoria actual y máximo.

La salida debería ser algo como:

```
Number of unique route string objects (with interning): 181
Current memory usage: 189.56 MB
Peak memory usage: 209.32 MB
```

Reiniciemos el intérprete e intentemos internar tanto las cadenas de ruta como las de fecha para ver si podemos reducir aún más el uso de memoria.

```python
exit()
```

Inicia Python nuevamente:

```bash
python3
```

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for both route and date columns
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, sys.intern, str, int])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage (interning route and date): {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage (interning route and date): {peak / 1024 / 1024:.2f} MB")
```

La salida debería mostrar una disminución adicional en el uso de memoria:

```
Current memory usage (interning route and date): 170.23 MB
Peak memory usage (interning route and date): 190.05 MB
```

Esto demuestra cómo comprender el modelo de memoria de Python y utilizar técnicas como el internamiento de cadenas puede ayudar a optimizar tus programas, especialmente cuando se trabaja con grandes conjuntos de datos que contienen valores repetidos.

Finalmente, sal del intérprete de Python:

```python
exit()
```
