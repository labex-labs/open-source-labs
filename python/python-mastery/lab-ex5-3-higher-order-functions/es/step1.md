# Comprendiendo la duplicación de código

Comencemos por observar el código actual en el archivo `reader.py`. En programación, examinar el código existente es un paso importante para entender cómo funcionan las cosas e identificar áreas de mejora. Puedes abrir el archivo `reader.py` en el WebIDE. Hay dos formas de hacer esto. Puedes hacer clic en el archivo en el explorador de archivos, o puedes ejecutar los siguientes comandos en la terminal. Estos comandos primero navegan al directorio del proyecto y luego muestran el contenido del archivo `reader.py`.

```bash
cd ~/project
cat reader.py
```

Cuando mires el código, notarás que hay dos funciones. Las funciones en Python son bloques de código que realizan una tarea específica. Aquí están las dos funciones y lo que hacen:

1. `csv_as_dicts()`: Esta función toma datos CSV y los convierte en una lista de diccionarios. Un diccionario en Python es una colección de pares clave - valor, que es útil para almacenar datos de manera estructurada.
2. `csv_as_instances()`: Esta función toma datos CSV y los convierte en una lista de instancias. Una instancia es un objeto creado a partir de una clase, que es un modelo para crear objetos.

Ahora, echemos un vistazo más detallado a estas dos funciones. Verás que son bastante similares. Ambas funciones siguen estos pasos:

- Primero, inicializan una lista `records` vacía. Una lista en Python es una colección de elementos que pueden ser de diferentes tipos. Inicializar una lista vacía significa crear una lista sin elementos, que se utilizará para almacenar los datos procesados.
- Luego, utilizan `csv.reader()` para analizar la entrada. Analizar significa analizar los datos de entrada para extraer información significativa. En este caso, `csv.reader()` nos ayuda a leer los datos CSV fila por fila.
- Manejan los encabezados de la misma manera. Los encabezados en un archivo CSV son la primera fila que generalmente contiene los nombres de las columnas.
- Después de eso, recorren cada fila en los datos CSV. Un bucle es una construcción de programación que te permite ejecutar un bloque de código varias veces.
- Para cada fila, la procesan para crear un registro. Este registro puede ser un diccionario o una instancia, dependiendo de la función.
- Añaden el registro a la lista `records`. Añadir significa agregar un elemento al final de la lista.
- Finalmente, devuelven la lista `records`, que contiene todos los datos procesados.

Esta duplicación de código es un problema por varias razones. Cuando el código se duplica:

- Se vuelve más difícil de mantener. Si necesitas hacer un cambio en el código, debes hacer el mismo cambio en múltiples lugares. Esto lleva más tiempo y esfuerzo.
- Cualquier cambio debe implementarse en múltiples lugares. Esto aumenta la posibilidad de que olvides hacer el cambio en uno de los lugares, lo que puede causar un comportamiento inconsistente.
- También aumenta la posibilidad de introducir errores. Los errores son fallos en el código que pueden hacer que se comporte de manera inesperada.

La única diferencia real entre estas dos funciones es cómo convierten una fila en un registro. Esta es una situación clásica en la que una función de orden superior puede ser muy útil. Una función de orden superior es una función que puede tomar otra función como argumento o devolver una función como resultado.

Veamos algunos ejemplos de uso de estas funciones para entender mejor cómo funcionan. El siguiente código muestra cómo usar `csv_as_dicts()` y `csv_as_instances()`:

```python
# Example of using csv_as_dicts
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # {'name': 'AA', 'shares': 100, 'price': 32.2}

# Example of using csv_as_instances
class Stock:
    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

with open('portfolio.csv') as f:
    portfolio = csv_as_instances(f, Stock)
print(portfolio[0].name, portfolio[0].shares, portfolio[0].price)  # AA 100 32.2
```

En el siguiente paso, crearemos una función de orden superior para eliminar esta duplicación de código. Esto hará que el código sea más mantenible y menos propenso a errores.
