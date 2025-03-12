# Variables de Clase y Herencia

En este paso, exploraremos cómo las variables de clase interactúan con la herencia y cómo pueden servir como un mecanismo de personalización. En Python, la herencia permite que una subclase herede atributos y métodos de una clase base. Las variables de clase son variables que pertenecen a la propia clase, no a ninguna instancia específica de la clase. Comprender cómo funcionan juntas es crucial para crear código flexible y mantenible.

## Variables de Clase en la Herencia

Cuando una subclase hereda de una clase base, automáticamente obtiene acceso a las variables de clase de la clase base. Sin embargo, una subclase tiene la capacidad de anular estas variables de clase. Al hacerlo, la subclase puede cambiar su comportamiento sin afectar a la clase base. Esta es una característica muy poderosa, ya que te permite personalizar el comportamiento de una subclase según tus necesidades específicas.

## Creación de una Clase Stock Especializada

Creemos una subclase de la clase `Stock`. La llamaremos `DStock`, que significa Decimal Stock (Stock decimal). La principal diferencia entre `DStock` y la clase `Stock` regular es que `DStock` utilizará el tipo `Decimal` para los valores de precio en lugar de `float`. En cálculos financieros, la precisión es extremadamente importante, y el tipo `Decimal` proporciona una aritmética decimal más precisa en comparación con `float`.

Para crear esta subclase, crearemos un nuevo archivo llamado `decimal_stock.py`. Aquí está el código que debes poner en este archivo:

```python
# decimal_stock.py
from decimal import Decimal
from stock import Stock

class DStock(Stock):
    """
    Una versión especializada de Stock que utiliza Decimal para los precios
    """
    types = (str, int, Decimal)  # Anular la variable de clase types

# Prueba la subclase
if __name__ == "__main__":
    # Crea un DStock a partir de datos de fila
    row = ['AA', '100', '32.20']
    ds = DStock.from_row(row)

    print(f"DStock: {ds.name}")
    print(f"Shares: {ds.shares}")
    print(f"Price: {ds.price} (type: {type(ds.price).__name__})")
    print(f"Cost: {ds.cost()} (type: {type(ds.cost()).__name__})")

    # Para comparación, crea un Stock regular a partir de los mismos datos
    s = Stock.from_row(row)
    print(f"\nRegular Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price} (type: {type(s.price).__name__})")
    print(f"Cost: {s.cost()} (type: {type(s.cost()).__name__})")
```

Después de crear el archivo `decimal_stock.py` con el código anterior, debes ejecutarlo para ver los resultados. Abre tu terminal y sigue estos pasos:

```bash
cd ~/project
python decimal_stock.py
```

Deberías ver una salida similar a esta:

```
DStock: AA
Shares: 100
Price: 32.20 (type: Decimal)
Cost: 3220.0 (type: Decimal)

Regular Stock: AA
Shares: 100
Price: 32.2 (type: float)
Cost: 3220.0 (type: float)
```

## Puntos Clave sobre Variables de Clase y Herencia

A partir de este ejemplo, podemos sacar varias conclusiones importantes:

1. La clase `DStock` hereda todos los métodos de la clase `Stock`, como el método `cost()`, sin tener que redefinirlos. Esta es una de las principales ventajas de la herencia, ya que te ahorra escribir código redundante.
2. Al simplemente anular la variable de clase `types`, hemos cambiado cómo se convierten los datos al crear nuevas instancias de `DStock`. Esto muestra cómo se pueden utilizar las variables de clase para personalizar el comportamiento de una subclase.
3. La clase base, `Stock`, permanece sin cambios y sigue funcionando con valores `float`. Esto significa que los cambios que hicimos en la subclase no afectan a la clase base, lo cual es un buen principio de diseño.
4. El método de clase `from_row()` funciona correctamente tanto con las clases `Stock` como `DStock`. Esto demuestra el poder de la herencia, ya que el mismo método se puede utilizar con diferentes subclases.

Este ejemplo muestra claramente cómo se pueden utilizar las variables de clase como un mecanismo de configuración. Las subclases pueden anular estas variables para personalizar su comportamiento sin tener que reescribir los métodos.

## Discusión sobre el Diseño

Consideremos un enfoque alternativo en el que colocamos las conversiones de tipo en el método `__init__`:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

Con este enfoque, podemos crear un objeto `Stock` a partir de una fila de datos de esta manera:

```python
row = ['AA', '100', '32.20']
s = Stock(*row)
```

Aunque este enfoque puede parecer más sencillo a primera vista, tiene varios inconvenientes:

1. Combina dos preocupaciones diferentes: la inicialización del objeto y la conversión de datos. Esto hace que el código sea más difícil de entender y mantener.
2. El método `__init__` se vuelve menos flexible porque siempre convierte las entradas, incluso si ya están en el tipo correcto.
3. Restringe cómo las subclases pueden personalizar el proceso de conversión. Las subclases tendrían más dificultades para cambiar la lógica de conversión si está incrustada en el método `__init__`.
4. El código se vuelve más frágil. Si alguna de las conversiones falla, el objeto no se puede crear, lo que puede provocar errores en tu programa.

Por otro lado, el enfoque del método de clase separa estas preocupaciones. Esto hace que el código sea más mantenible y flexible, ya que cada parte del código tiene una única responsabilidad.
