# Mejorando el contenedor personalizado para el rebanado (slicing)

Nuestro contenedor personalizado es excelente para acceder a registros individuales. Sin embargo, hay un problema cuando se trata de hacer rebanados (slicing). Cuando intentas tomar una rebanada de nuestro contenedor, el resultado no es lo que normalmente esperarías.

Entendamos por qué sucede esto. En Python, el rebanado es una operación común utilizada para extraer una porción de una secuencia. Pero para nuestro contenedor personalizado, Python no sabe cómo crear un nuevo objeto `RideData` solo con los datos rebanados. En lugar de eso, crea una lista que contiene los resultados de llamar a `__getitem__` para cada índice en la rebanada.

1. Probemos el rebanado en la shell de Python:

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # This will likely be a list, not a RideData object
print(r)  # This might look like a list of numbers, not dictionaries
```

En este código, primero importamos el módulo `readrides`. Luego leemos los datos del archivo `ctabus.csv` en una variable `rows`. Cuando intentamos tomar una rebanada de los primeros 10 registros y comprobamos el tipo del resultado, encontramos que es una lista en lugar de un objeto `RideData`. Imprimir el resultado puede mostrar algo inesperado, como una lista de números en lugar de diccionarios.

2. Modifiquemos nuestra clase `RideData` para manejar el rebanado adecuadamente. Abrir `readrides.py` y actualizar el método `__getitem__`:

```python
def __getitem__(self, index):
    if isinstance(index, slice):
        # Handle slice
        result = RideData()
        result.routes = self.routes[index]
        result.dates = self.dates[index]
        result.daytypes = self.daytypes[index]
        result.numrides = self.numrides[index]
        return result
    else:
        # Handle single index
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}
```

En este método `__getitem__` actualizado, primero comprobamos si el `index` es una rebanada. Si lo es, creamos un nuevo objeto `RideData` llamado `result`. Luego llenamos este nuevo objeto con rebanadas de las columnas de datos originales (`routes`, `dates`, `daytypes` y `numrides`). Esto asegura que cuando rebanamos nuestro contenedor personalizado, obtengamos otro objeto `RideData` en lugar de una lista. Si el `index` no es una rebanada (es decir, es un solo índice), devolvemos un diccionario que contiene el registro relevante.

3. Probemos nuestra capacidad mejorada de rebanado:

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # Should now be readrides.RideData
len(r)   # Should be 10
r[0]     # Should be the same as rows[0]
r[1]     # Should be the same as rows[1]
```

Después de actualizar el método `__getitem__`, podemos probar el rebanado nuevamente. Cuando tomamos una rebanada de los primeros 10 registros, el tipo del resultado ahora debe ser `readrides.RideData`. La longitud de la rebanada debe ser 10, y acceder a elementos individuales en la rebanada debe darnos los mismos resultados que acceder a los elementos correspondientes en el contenedor original.

4. También puedes probar con diferentes patrones de rebanado:

```python
# Get every other record from the first 20
r2 = rows[0:20:2]
len(r2)  # Should be 10

# Get the last 10 records
r3 = rows[-10:]
len(r3)  # Should be 10
```

Aquí, estamos probando diferentes patrones de rebanado. La primera rebanada `rows[0:20:2]` obtiene cada otro registro de los primeros 20 registros, y la longitud de la rebanada resultante debe ser 10. La segunda rebanada `rows[-10:]` obtiene los últimos 10 registros, y su longitud también debe ser 10.

Al implementar adecuadamente el rebanado, nuestro contenedor personalizado ahora se comporta aún más como una lista estándar de Python, mientras mantiene la eficiencia de memoria del almacenamiento orientado a columnas.

Este enfoque de crear clases de contenedores personalizados que imitan los contenedores incorporados de Python pero con diferentes representaciones internas es una técnica poderosa para optimizar el uso de memoria sin cambiar la interfaz que tu código presenta a los usuarios.
