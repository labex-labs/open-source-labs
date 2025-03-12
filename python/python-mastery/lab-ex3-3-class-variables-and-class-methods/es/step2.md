# Implementación de Constructores Alternativos con Métodos de Clase

En este paso, aprenderemos cómo implementar un constructor alternativo utilizando un método de clase. Esto nos permitirá crear objetos `Stock` a partir de datos de filas CSV de una manera más elegante.

## ¿Qué es un Constructor Alternativo?

En Python, un constructor alternativo es un patrón útil. Por lo general, creamos objetos utilizando el método estándar `__init__`. Sin embargo, un constructor alternativo nos da una forma adicional de crear objetos. Los métodos de clase son muy adecuados para implementar constructores alternativos porque pueden acceder a la propia clase.

## Implementación del Método de Clase from_row()

Agregaremos una variable de clase `types` y un método de clase `from_row()` a nuestra clase `Stock`. Esto simplificará el proceso de creación de instancias de `Stock` a partir de datos CSV.

Modifiquemos el archivo `stock.py` agregando el código resaltado:

```python
# stock.py

class Stock:
    types = (str, int, float)  # Conversiones de tipo a aplicar a los datos CSV

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    @classmethod
    def from_row(cls, row):
        """
        Crea una instancia de Stock a partir de una fila de datos CSV.

        Argumentos:
            row: Una lista de cadenas [nombre, acciones, precio]

        Devuelve:
            Una nueva instancia de Stock
        """
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

# El resto del archivo permanece sin cambios
```

Ahora, entendamos paso a paso lo que está sucediendo en este código:

1. Definimos una variable de clase `types`. Es una tupla que contiene funciones de conversión de tipo `(str, int, float)`. Estas funciones se utilizarán para convertir los datos de la fila CSV a los tipos adecuados.
2. Agregamos un método de clase `from_row()`. El decorador `@classmethod` marca este método como un método de clase.
3. El primer parámetro de este método es `cls`, que es una referencia a la propia clase. En métodos normales, usamos `self` para referirnos a una instancia de la clase, pero aquí usamos `cls` porque es un método de clase.
4. La función `zip()` se utiliza para emparejar cada función de conversión de tipo en `types` con el valor correspondiente en la lista `row`.
5. Usamos una comprensión de lista para aplicar cada función de conversión al valor correspondiente en la lista `row`. De esta manera, convertimos los datos de cadena de la fila CSV a los tipos adecuados.
6. Finalmente, creamos una nueva instancia de la clase `Stock` utilizando los valores convertidos y la devolvemos.

## Prueba del Constructor Alternativo

Ahora, crearemos un nuevo archivo llamado `test_class_method.py` para probar nuestro nuevo método de clase. Esto nos ayudará a verificar que el constructor alternativo funcione como se espera.

```python
# test_class_method.py
from stock import Stock

# Prueba el método de clase from_row()
row = ['AA', '100', '32.20']
s = Stock.from_row(row)

print(f"Stock: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost()}")

# Prueba con una fila diferente
row2 = ['GOOG', '50', '1120.50']
s2 = Stock.from_row(row2)

print(f"\nStock: {s2.name}")
print(f"Shares: {s2.shares}")
print(f"Price: {s2.price}")
print(f"Cost: {s2.cost()}")
```

Para ver los resultados, ejecuta los siguientes comandos en tu terminal:

```bash
cd ~/project
python test_class_method.py
```

Deberías ver una salida similar a esta:

```
Stock: AA
Shares: 100
Price: 32.2
Cost: 3220.0

Stock: GOOG
Shares: 50
Price: 1120.5
Cost: 56025.0
```

Observa que ahora podemos crear instancias de `Stock` directamente a partir de datos de cadena sin tener que realizar manualmente conversiones de tipo fuera de la clase. Esto hace que nuestro código sea más limpio y asegura que la responsabilidad de la conversión de datos se maneje dentro de la propia clase.
