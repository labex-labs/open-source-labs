# Desafío de Análisis de Datos con Datos de la Autoridad de Transporte de Chicago

Ahora que has practicado el trabajo con diferentes estructuras de datos de Python y el módulo `collections`, es hora de poner estas habilidades en práctica en una tarea real de análisis de datos. En este experimento, analizaremos los datos de pasajeros de autobús de la Autoridad de Transporte de Chicago (CTA, por sus siglas en inglés). Esta aplicación práctica te ayudará a entender cómo usar Python para extraer información significativa de conjuntos de datos del mundo real.

## Comprendiendo los Datos

Primero, echemos un vistazo a los datos de transporte con los que trabajaremos. En tu terminal de Python, ejecutarás algún código para cargar los datos y entender su estructura básica.

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>> print(len(rows))
# This will show the number of records in the dataset

>>> # Let's look at the first record to understand the structure
>>> import pprint
>>> pprint.pprint(rows[0])
```

La declaración `import readrides` importa un módulo personalizado que tiene una función para leer los datos del archivo CSV. La función `readrides.read_rides_as_dicts` lee los datos del archivo CSV especificado y convierte cada fila en un diccionario. `len(rows)` nos da el número total de registros en el conjunto de datos. Al imprimir el primer registro usando `pprint.pprint(rows[0])`, podemos ver claramente la estructura de cada registro.

Los datos contienen registros diarios de pasajeros para diferentes rutas de autobús. Cada registro incluye:

- `route`: El número de la ruta de autobús
- `date`: La fecha en formato "YYYY - MM - DD"
- `daytype`: Ya sea "W" para día laboral, "A" para sábado o "U" para domingo/festivo
- `rides`: El número de pasajeros ese día

## Tareas de Análisis

Resolvamos cada una de las preguntas del desafío una por una:

### Pregunta 1: ¿Cuántas rutas de autobús existen en Chicago?

Para responder a esta pregunta, necesitamos encontrar todos los números de ruta únicos en el conjunto de datos. Usaremos una comprensión de conjunto para esta tarea.

```python
>>> # Get all unique route numbers using a set comprehension
>>> unique_routes = {row['route'] for row in rows}
>>> print(len(unique_routes))
```

Una comprensión de conjunto es una forma concisa de crear un conjunto. En este caso, iteramos sobre cada fila en la lista `rows` y extraemos el valor de `route`. Dado que un conjunto solo almacena elementos únicos, terminamos con un conjunto de todos los números de ruta únicos. Imprimir la longitud de este conjunto nos da el número total de rutas de autobús únicas.

También podemos ver cuáles son algunas de estas rutas:

```python
>>> # Print a few of the route numbers
>>> print(list(unique_routes)[:10])
```

Aquí, convertimos el conjunto de rutas únicas en una lista y luego imprimimos los primeros 10 elementos de esa lista.

### Pregunta 2: ¿Cuántas personas tomaron el autobús número 22 el 2 de febrero de 2011?

Para esta pregunta, necesitamos filtrar los datos para encontrar el registro específico que coincide con la ruta y la fecha dadas.

```python
>>> # Find rides on route 22 on February 2, 2011
>>> target_date = "2011-02-02"
>>> target_route = "22"
>>>
>>> for row in rows:
...     if row['route'] == target_route and row['date'] == target_date:
...         print(f"Rides on route {target_route} on {target_date}: {row['rides']}")
...         break
```

Primero definimos las variables `target_date` y `target_route`. Luego, iteramos sobre cada fila en la lista `rows`. Para cada fila, comprobamos si la `route` y la `date` coinciden con nuestros valores objetivo. Si se encuentra una coincidencia, imprimimos el número de pasajeros y salimos del bucle ya que hemos encontrado el registro que buscábamos.

Puedes modificar esto para comprobar cualquier ruta en cualquier fecha cambiando las variables `target_date` y `target_route`.

### Pregunta 3: ¿Cuál es el número total de pasajeros en cada ruta de autobús?

Usemos un `Counter` para calcular el total de pasajeros por ruta. Un `Counter` es una subclase de diccionario del módulo `collections` que se utiliza para contar objetos hashables.

```python
>>> from collections import Counter
>>>
>>> # Initialize a counter
>>> total_rides_by_route = Counter()
>>>
>>> # Sum up rides for each route
>>> for row in rows:
...     total_rides_by_route[row['route']] += row['rides']
...
>>> # View the top 5 routes by total ridership
>>> for route, rides in total_rides_by_route.most_common(5):
...     print(f"Route {route}: {rides:,} total rides")
```

Primero importamos la clase `Counter` del módulo `collections`. Luego, inicializamos un contador vacío llamado `total_rides_by_route`. A medida que iteramos sobre cada fila en la lista `rows`, agregamos el número de pasajeros de cada ruta al contador. Finalmente, usamos el método `most_common(5)` para obtener las 5 rutas con el mayor número total de pasajeros y imprimimos los resultados.

### Pregunta 4: ¿Qué cinco rutas de autobús tuvieron el mayor aumento de pasajeros en diez años, desde 2001 hasta 2011?

Esta es una tarea más compleja. Necesitamos comparar el número de pasajeros en 2001 con el de 2011 para cada ruta.

```python
>>> # Create dictionaries to store total annual rides by route
>>> rides_2001 = Counter()
>>> rides_2011 = Counter()
>>>
>>> # Collect data for each year
>>> for row in rows:
...     if row['date'].startswith('2001-'):
...         rides_2001[row['route']] += row['rides']
...     elif row['date'].startswith('2011-'):
...         rides_2011[row['route']] += row['rides']
...
>>> # Calculate increases
>>> increases = {}
>>> for route in unique_routes:
...     if route in rides_2001 and route in rides_2011:
...         increase = rides_2011[route] - rides_2001[route]
...         increases[route] = increase
...
>>> # Find the top 5 routes with the biggest increases
>>> import heapq
>>> top_5_increases = heapq.nlargest(5, increases.items(), key=lambda x: x[1])
>>>
>>> # Display the results
>>> print("Top 5 routes with the greatest ridership increase from 2001 to 2011:")
>>> for route, increase in top_5_increases:
...     print(f"Route {route}: increased by {increase:,} rides")
...     print(f"  2001 rides: {rides_2001[route]:,}")
...     print(f"  2011 rides: {rides_2011[route]:,}")
...     print()
```

Primero creamos dos objetos `Counter`, `rides_2001` y `rides_2011`, para almacenar el total de pasajeros de cada ruta en 2001 y 2011 respectivamente. A medida que iteramos sobre cada fila en la lista `rows`, comprobamos si la fecha comienza con '2001 -' o '2011 -' y agregamos los pasajeros al contador correspondiente.

Luego, creamos un diccionario vacío `increases` para almacenar el aumento de pasajeros de cada ruta. Iteramos sobre las rutas únicas y calculamos el aumento restando los pasajeros de 2001 de los de 2011 para cada ruta.

Para encontrar las 5 rutas con los mayores aumentos, usamos la función `heapq.nlargest`. Esta función toma el número de elementos a devolver (5 en este caso), el iterable (`increases.items()`) y una función clave (`lambda x: x[1]`) que especifica cómo comparar los elementos.

Finalmente, imprimimos los resultados, mostrando el número de la ruta, el aumento de pasajeros y el número de pasajeros en 2001 y 2011.

Este análisis identifica qué rutas de autobús experimentaron el mayor crecimiento en el número de pasajeros durante la década, lo que podría indicar cambios en los patrones de población, mejoras en el servicio u otras tendencias interesantes.

Puedes extender estos análisis de muchas maneras. Por ejemplo, podrías querer:

- Analizar los patrones de pasajeros por día de la semana
- Encontrar rutas con una disminución en el número de pasajeros
- Comparar las variaciones estacionales en el número de pasajeros

Las técnicas que has aprendido en este laboratorio proporcionan una base sólida para este tipo de exploración y análisis de datos.
