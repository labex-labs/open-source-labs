# Creación de un Lector de CSV de Propósito General

En este último paso, crearemos una función de propósito general. Esta función será capaz de leer archivos CSV y crear objetos de cualquier clase que haya implementado el método de clase `from_row()`. Esto nos muestra el poder de utilizar métodos de clase como una interfaz uniforme. Una interfaz uniforme significa que diferentes clases pueden utilizarse de la misma manera, lo que hace que nuestro código sea más flexible y fácil de gestionar.

## Modificación de la Función read_portfolio()

Primero, actualizaremos la función `read_portfolio()` en el archivo `stock.py`. Utilizaremos nuestro nuevo método de clase `from_row()`. Abre el archivo `stock.py` y cambia la función `read_portfolio()` de la siguiente manera:

```python
def read_portfolio(filename):
    '''
    Lee un archivo de cartera de acciones en una lista de instancias de Stock
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Omite la cabecera
        for row in rows:
            portfolio.append(Stock.from_row(row))
    return portfolio
```

Esta nueva versión de la función es más sencilla. Le da la responsabilidad de la conversión de tipos a la clase `Stock`, donde realmente pertenece. La conversión de tipos significa cambiar los datos de un tipo a otro, como convertir una cadena en un entero. Al hacer esto, hacemos que nuestro código sea más organizado y fácil de entender.

## Creación de un Lector de CSV de Propósito General

Ahora, crearemos una función de propósito más general en el archivo `reader.py`. Esta función puede leer datos CSV y crear instancias de cualquier clase que tenga un método de clase `from_row()`.

Abre el archivo `reader.py` y agrega la siguiente función:

```python
def read_csv_as_instances(filename, cls):
    '''
    Lee un archivo CSV en una lista de instancias de la clase dada.

    Argumentos:
        filename: Nombre del archivo CSV
        cls: Clase a instanciar (debe tener el método de clase from_row)

    Devuelve:
        Lista de instancias de clase
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Omite la cabecera
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

Esta función toma dos entradas: un nombre de archivo y una clase. Luego devuelve una lista de instancias de esa clase, creadas a partir de los datos en el archivo CSV. Esto es muy útil porque podemos usarlo con diferentes clases, siempre que tengan el método `from_row()`.

## Prueba del Lector de CSV de Propósito General

Creemos un archivo de prueba para ver cómo funciona nuestro lector de propósito general. Crea un archivo llamado `test_csv_reader.py` con el siguiente contenido:

```python
# test_csv_reader.py
from reader import read_csv_as_instances
from stock import Stock
from decimal_stock import DStock

# Lee la cartera como instancias de Stock
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print(f"La cartera contiene {len(portfolio)} acciones")
print(f"Primera acción: {portfolio[0].name}, {portfolio[0].shares} acciones a ${portfolio[0].price}")

# Lee la cartera como instancias de DStock (con precios en Decimal)
decimal_portfolio = read_csv_as_instances('portfolio.csv', DStock)
print(f"\nLa cartera decimal contiene {len(decimal_portfolio)} acciones")
print(f"Primera acción: {decimal_portfolio[0].name}, {decimal_portfolio[0].shares} acciones a ${decimal_portfolio[0].price}")

# Define una nueva clase para leer los datos de autobús
class BusRide:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

    @classmethod
    def from_row(cls, row):
        return cls(row[0], row[1], row[2], int(row[3]))

# Lee algunos datos de autobús (solo los primeros 5 registros por brevedad)
print("\nLeyendo datos de autobús...")
import csv
with open('ctabus.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Omite la cabecera
    bus_rides = []
    for i, row in enumerate(rows):
        if i >= 5:  # Solo lee 5 registros para el ejemplo
            break
        bus_rides.append(BusRide.from_row(row))

# Muestra los datos de autobús
for ride in bus_rides:
    print(f"Ruta: {ride.route}, Fecha: {ride.date}, Tipo: {ride.daytype}, Viajes: {ride.rides}")
```

Ejecuta este archivo para ver los resultados. Abre tu terminal y utiliza los siguientes comandos:

```bash
cd ~/project
python test_csv_reader.py
```

Deberías ver una salida que muestre los datos de la cartera cargados como instancias de `Stock` y `DStock`, y los datos de la ruta de autobús cargados como instancias de `BusRide`. Esto demuestra que nuestro lector de propósito general funciona con diferentes clases.

## Principales Beneficios de Este Enfoque

Este enfoque muestra varios conceptos poderosos:

1. **Separación de preocupaciones**: Leer datos está separado de crear objetos. Esto significa que el código para leer el archivo CSV no se mezcla con el código para crear objetos. Hace que el código sea más fácil de entender y mantener.
2. **Polimorfismo**: El mismo código puede funcionar con diferentes clases que sigan la misma interfaz. En nuestro caso, siempre que una clase tenga el método `from_row()`, nuestro lector de propósito general puede utilizarla.
3. **Flexibilidad**: Podemos cambiar fácilmente cómo se convierten los datos utilizando diferentes clases. Por ejemplo, podemos usar `Stock` o `DStock` para manejar los datos de la cartera de manera diferente.
4. **Extensibilidad**: Podemos agregar nuevas clases que funcionen con nuestro lector sin cambiar el código del lector. Esto hace que nuestro código sea más resistente al paso del tiempo.

Este es un patrón común en Python que hace que el código sea más modular, reutilizable y mantenible.

## Notas Finales sobre Métodos de Clase

Los métodos de clase se utilizan a menudo como constructores alternativos en Python. Por lo general, puedes distinguirlos porque sus nombres a menudo tienen la palabra "from" en ellos. Por ejemplo:

```python
# Algunos ejemplos de tipos integrados de Python
dict.fromkeys(['a', 'b', 'c'], 0)  # Crea un diccionario con valores predeterminados
datetime.datetime.fromtimestamp(1627776000)  # Crea una fecha y hora a partir de una marca de tiempo
int.from_bytes(b'\x00\x01', byteorder='big')  # Crea un entero a partir de bytes
```

Siguiendo esta convención, haces que tu código sea más legible y consistente con las bibliotecas integradas de Python. Esto ayuda a otros desarrolladores a entender tu código más fácilmente.
