# Explorando la Herencia de Metaclases

Las metaclases tienen una característica fascinante: son "pegajosas". Esto significa que una vez que una clase utiliza una metaclase, todas sus subclases en la jerarquía de herencia también utilizarán la misma metaclase. En otras palabras, la propiedad de la metaclase se propaga a lo largo de la cadena de herencia.

Veamos esto en acción:

1. Primero, abre el archivo `mymeta.py`. Al final de este archivo, vamos a agregar una nueva clase. Esta clase, llamada `MyStock`, heredará de la clase `Stock`. El método `__init__` se utiliza para inicializar los atributos del objeto, y llamamos al método `__init__` de la clase padre utilizando `super().__init__` para inicializar los atributos comunes. El método `info` se utiliza para devolver una cadena formateada con información sobre las acciones. Agrega el siguiente código:

```python
class MyStock(Stock):
    def __init__(self, name, shares, price, category):
        super().__init__(name, shares, price)
        self.category = category

    def info(self):
        return f"{self.name} ({self.category}): {self.shares} shares at ${self.price}"
```

2. Después de agregar el código, guarda el archivo `mymeta.py`. Guardar el archivo asegura que los cambios que hicimos se almacenen y se puedan utilizar más tarde.

3. Ahora, crearemos un nuevo archivo llamado `test_inheritance.py` para probar el comportamiento de herencia de la metaclase. En este archivo, importaremos la clase `MyStock` del archivo `mymeta.py`. Luego, crearemos una instancia de la clase `MyStock`, llamaremos a sus métodos e imprimiremos los resultados para ver cómo funciona la metaclase a través de la herencia. Agrega el siguiente código a `test_inheritance.py`:

```python
# test_inheritance.py
from mymeta import MyStock

# Create a MyStock instance
tech_stock = MyStock("MSFT", 50, 305.75, "Technology")

# Test the methods
print(tech_stock.info())
print(f"Total cost: ${tech_stock.cost()}")

# Sell some shares
tech_stock.sell(5)
print(f"After selling: {tech_stock.shares} shares remaining")
print(f"Updated cost: ${tech_stock.cost()}")
```

4. Finalmente, ejecuta el archivo `test_inheritance.py` para ver la metaclase en acción a través de la herencia. Abre tu terminal, navega al directorio donde se encuentra el archivo `test_inheritance.py` y ejecuta el siguiente comando:

```bash
python3 test_inheritance.py
```

Deberías ver una salida similar a:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Creating class : MyStock
Base classes   : (<class 'mymeta.Stock'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'info', '__doc__']
MSFT (Technology): 50 shares at $305.75
Total cost: $15287.5
After selling: 45 shares remaining
Updated cost: $13758.75
```

Observa que aunque no especificamos explícitamente una metaclase para la clase `MyStock`, la metaclase todavía se aplica. Esto demuestra claramente cómo las metaclases se propagan a través de la herencia.

## Usos Prácticos de las Metaclases

En nuestro ejemplo, la metaclase simplemente imprime información sobre las clases. Sin embargo, las metaclases tienen muchas aplicaciones prácticas en la programación del mundo real:

1. **Validación**: Puedes utilizar metaclases para verificar si una clase tiene los métodos o atributos requeridos. Esto ayuda a garantizar que las clases cumplan con ciertos criterios antes de ser utilizadas.
2. **Registro**: Las metaclases pueden registrar automáticamente las clases en un registro. Esto es útil cuando necesitas llevar un seguimiento de todas las clases de un cierto tipo.
3. **Cumplimiento de interfaces**: Se pueden utilizar para garantizar que las clases implementen las interfaces requeridas. Esto ayuda a mantener una estructura consistente en tu código.
4. **Programación orientada a aspectos**: Las metaclases pueden agregar comportamientos a los métodos. Por ejemplo, puedes agregar registro o monitoreo de rendimiento a los métodos sin modificar directamente el código del método.
5. **Sistemas ORM**: En los sistemas de mapeo objeto - relacional (ORM) como Django o SQLAlchemy, se utilizan metaclases para mapear clases a tablas de base de datos. Esto simplifica las operaciones de base de datos en tu aplicación.

Las metaclases son muy poderosas, pero deben usarse con moderación. Como dijo una vez Tim Peters (famoso por el Zen de Python), "Las metaclases son una magia más profunda de la que el 99% de los usuarios debería preocuparse".
