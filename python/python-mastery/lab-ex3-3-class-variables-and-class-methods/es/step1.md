# Comprensión de Variables de Clase y Métodos de Clase

En este primer paso, vamos a profundizar en los conceptos de variables de clase y métodos de clase en Python. Estos son conceptos importantes que te ayudarán a escribir código más eficiente y organizado. Antes de comenzar a trabajar con variables de clase y métodos de clase, primero echemos un vistazo a cómo se crean actualmente las instancias de nuestra clase `Stock`. Esto nos dará una comprensión básica y nos mostrará dónde podemos hacer mejoras.

## ¿Qué son las Variables de Clase?

Las variables de clase son un tipo especial de variables en Python. Son compartidas entre todas las instancias de una clase. Para entender esto mejor, comparemoslas con las variables de instancia. Las variables de instancia son únicas para cada instancia de una clase. Por ejemplo, si tienes múltiples instancias de una clase, cada instancia puede tener su propio valor para una variable de instancia. Por otro lado, las variables de clase se definen a nivel de clase. Esto significa que todas las instancias de esa clase pueden acceder y compartir el mismo valor de la variable de clase.

## ¿Qué son los Métodos de Clase?

Los métodos de clase son métodos que trabajan en la propia clase, no en instancias individuales de la clase. Están vinculados a la clase, lo que significa que se pueden llamar directamente en la clase sin crear una instancia. Para definir un método de clase en Python, usamos el decorador `@classmethod`. Y en lugar de tomar la instancia (`self`) como primer parámetro, los métodos de clase toman la clase (`cls`) como su primer parámetro. Esto les permite operar en datos a nivel de clase y realizar acciones relacionadas con la clase en su conjunto.

## Enfoque Actual para Crear Instancias de Stock

Primero, veamos cómo se crean actualmente las instancias de la clase `Stock`. Abre el archivo `stock.py` en el editor para observar la implementación actual:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
```

Las instancias de esta clase se crean típicamente de una de estas maneras:

1. Inicialización directa con valores:

   ```python
   s = Stock('GOOG', 100, 490.1)
   ```

   Aquí, estamos creando directamente una instancia de la clase `Stock` proporcionando los valores para los atributos `name`, `shares` y `price`. Esta es una forma sencilla de crear una instancia cuando conoces los valores de antemano.

2. Creación a partir de datos leídos de un archivo CSV:
   ```python
   import csv
   with open('portfolio.csv') as f:
       rows = csv.reader(f)
       headers = next(rows)  # Saltar el encabezado
       row = next(rows)      # Obtener la primera fila de datos
       s = Stock(row[0], int(row[1]), float(row[2]))
   ```
   Cuando leemos datos de un archivo CSV, los valores están inicialmente en formato de cadena. Entonces, cuando creamos una instancia de `Stock` a partir de datos CSV, necesitamos convertir manualmente los valores de cadena a los tipos adecuados. Por ejemplo, el valor de `shares` debe convertirse a un entero, y el valor de `price` debe convertirse a un flotante.

Intentemos esto. Crea un nuevo archivo de Python llamado `test_stock.py` en el directorio `~/project` con el siguiente contenido:

```python
# test_stock.py
from stock import Stock
import csv

# Método 1: Creación directa
s1 = Stock('GOOG', 100, 490.1)
print(f"Stock: {s1.name}, Shares: {s1.shares}, Price: {s1.price}")
print(f"Cost: {s1.cost()}")

# Método 2: Creación a partir de una fila CSV
with open('portfolio.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Saltar el encabezado
    row = next(rows)      # Obtener la primera fila de datos
    s2 = Stock(row[0], int(row[1]), float(row[2]))
    print(f"\nStock from CSV: {s2.name}, Shares: {s2.shares}, Price: {s2.price}")
    print(f"Cost: {s2.cost()}")
```

Ejecuta este archivo para ver los resultados:

```bash
cd ~/project
python test_stock.py
```

Deberías ver una salida similar a:

```
Stock: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0

Stock from CSV: AA, Shares: 100, Price: 32.2
Cost: 3220.0
```

Esta conversión manual funciona, pero tiene algunos inconvenientes. Necesitamos conocer el formato exacto de los datos y debemos realizar las conversiones cada vez que creamos una instancia a partir de datos CSV. Esto puede ser propenso a errores y consumir mucho tiempo. En el siguiente paso, crearemos una solución más elegante utilizando métodos de clase.
