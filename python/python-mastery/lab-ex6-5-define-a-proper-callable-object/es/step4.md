# Desafío: Usar un objeto invocable como método

En Python, cuando se utiliza un objeto invocable (callable object) como un método dentro de una clase, hay un desafío único que se debe abordar. Un objeto invocable es algo que se puede "llamar" como una función, como una función en sí o un objeto con un método `__call__`. Cuando se utiliza como un método de clase, no siempre funciona como se espera debido a cómo Python pasa la instancia (`self`) como el primer argumento.

Exploremos este problema creando una clase `Stock`. Esta clase representará una acción con atributos como el nombre, el número de acciones y el precio. También usaremos un validador para asegurarnos de que los datos con los que trabajamos son correctos.

Primero, abre el archivo `stock.py` para comenzar a escribir nuestra clase `Stock`. Puedes usar el siguiente comando para abrir el archivo en un editor:

```bash
code /home/labex/project/stock.py
```

Ahora, agrega el siguiente código al archivo `stock.py`. Este código define la clase `Stock` con un método `__init__` para inicializar los atributos de la acción, una propiedad `cost` para calcular el costo total y un método `sell` para reducir el número de acciones. También intentaremos usar `ValidatedFunction` para validar la entrada del método `sell`.

```python
from validate import ValidatedFunction, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: Integer):
        self.shares -= nshares

    # Try to use ValidatedFunction
    sell = ValidatedFunction(sell)
```

Después de definir la clase `Stock`, necesitamos probarla para ver si funciona como se espera. Crea un archivo de prueba llamado `test_stock.py` y ábrelo usando el siguiente comando:

```bash
code /home/labex/project/test_stock.py
```

Agrega el siguiente código al archivo `test_stock.py`. Este código crea una instancia de la clase `Stock`, imprime el número inicial de acciones y el costo, intenta vender algunas acciones y luego imprime el número actualizado de acciones y el costo.

```python
from stock import Stock

try:
    # Create a stock
    s = Stock('GOOG', 100, 490.1)

    # Get the initial cost
    print(f"Initial shares: {s.shares}")
    print(f"Initial cost: ${s.cost}")

    # Try to sell some shares
    s.sell(10)

    # Check the updated cost
    print(f"After selling, shares: {s.shares}")
    print(f"After selling, cost: ${s.cost}")

except Exception as e:
    print(f"Error: {e}")
```

Ahora, ejecuta el archivo de prueba usando el siguiente comando:

```bash
python3 /home/labex/project/test_stock.py
```

Probablemente encontrarás un error similar a:

```
Error: missing a required argument: 'nshares'
```

Este error ocurre porque cuando Python llama a un método como `s.sell(10)`, en realidad llama a `Stock.sell(s, 10)` detrás de escena. El parámetro `self` representa la instancia de la clase y se pasa automáticamente como el primer argumento. Sin embargo, nuestra `ValidatedFunction` no maneja correctamente este parámetro `self` porque no sabe que se está usando como un método.

**Comprendiendo el problema**

Cuando se define un método dentro de una clase y luego se reemplaza con una `ValidatedFunction`, en esencia se está envolviendo el método original. El problema es que el método envuelto no maneja automáticamente el parámetro `self` correctamente. Espera los argumentos de una manera que no tiene en cuenta que la instancia se pasa como el primer argumento.

**Solucionando el problema**

Para solucionar este problema, necesitamos modificar la forma en que manejamos los métodos. Crearemos una nueva clase llamada `ValidatedMethod` que pueda manejar correctamente las llamadas a métodos. Agrega el siguiente código al final del archivo `validate.py`:

```python
import inspect

class ValidatedMethod:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __get__(self, instance, owner):
        # This method is called when the attribute is accessed as a method
        if instance is None:
            return self

        # Return a callable that binds 'self' to the instance
        def method_wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)

        return method_wrapper

    def __call__(self, instance, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(instance, *args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(instance, *args, **kwargs)
```

Ahora, necesitamos modificar la clase `Stock` para usar `ValidatedMethod` en lugar de `ValidatedFunction`. Abre el archivo `stock.py` nuevamente:

```bash
code /home/labex/project/stock.py
```

Actualiza la clase `Stock` de la siguiente manera:

```python
from validate import ValidatedMethod, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @ValidatedMethod
    def sell(self, nshares: Integer):
        self.shares -= nshares
```

La clase `ValidatedMethod` es un descriptor (descriptor), que es un tipo especial de objeto en Python que puede cambiar cómo se accede a los atributos. El método `__get__` se llama cuando se accede al atributo como un método. Devuelve un objeto invocable que pasa correctamente la instancia como el primer argumento.

Ejecuta el archivo de prueba nuevamente usando el siguiente comando:

```bash
python3 /home/labex/project/test_stock.py
```

Ahora deberías ver una salida similar a:

```
Initial shares: 100
Initial cost: $49010.0
After selling, shares: 90
After selling, cost: $44109.0
```

Este desafío te ha mostrado un aspecto importante de los objetos invocables. Cuando se usan como métodos en una clase, requieren un manejo especial. Al implementar el protocolo de descriptor con el método `__get__`, podemos crear objetos invocables que funcionen correctamente tanto como funciones independientes como como métodos.
