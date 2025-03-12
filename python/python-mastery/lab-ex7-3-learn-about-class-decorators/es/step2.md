# Creación de un decorador de clase para validación

En el paso anterior, nuestra implementación funcionó, pero había una redundancia. Teníamos que especificar tanto la tupla `_fields` como los atributos descriptor. Esto no es muy eficiente y podemos mejorarlo. En Python, los decoradores de clase son una herramienta poderosa que puede ayudarnos a simplificar este proceso. Un decorador de clase es una función que toma una clase como argumento, la modifica de alguna manera y luego devuelve la clase modificada. Al usar un decorador de clase, podemos extraer automáticamente la información de los campos de los descriptores, lo que hará nuestro código más limpio y mantenible.

Vamos a crear un decorador de clase para simplificar nuestro código. Estos son los pasos que debes seguir:

1. Primero, abre el archivo `structure.py`. Puedes usar el siguiente comando en la terminal:

```bash
code ~/project/structure.py
```

Este comando abrirá el archivo `structure.py` en tu editor de código.

2. A continuación, agrega el siguiente código en la parte superior del archivo `structure.py`, justo después de cualquier declaración de importación. Este código define nuestro decorador de clase:

```python
from validate import Validator

def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields list automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

Analicemos lo que hace este decorador:

- Primero crea una lista vacía llamada `validators`. Luego, itera sobre todos los atributos de la clase usando `vars(cls).items()`. Si un atributo es una instancia de la clase `Validator`, agrega ese atributo a la lista `validators`.
- Después de eso, establece el atributo `_fields` de la clase. Crea una lista de nombres a partir de los validadores en la lista `validators` y la asigna a `cls._fields`.
- Finalmente, llama al método `create_init()` de la clase para generar el método `__init__` y luego devuelve la clase modificada.

3. Una vez que hayas agregado el código, guarda el archivo `structure.py`. Guardar el archivo asegura que tus cambios se conserven.

4. Ahora, necesitamos modificar nuestro archivo `stock.py` para usar este nuevo decorador. Abre el archivo `stock.py` usando el siguiente comando:

```bash
code ~/project/stock.py
```

5. Actualiza el archivo `stock.py` para usar el decorador `validate_attributes`. Reemplaza el código existente con lo siguiente:

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Observa los cambios que hemos hecho:

- Agregamos el decorador `@validate_attributes` justo encima de la definición de la clase `Stock`. Esto le dice a Python que aplique el decorador `validate_attributes` a la clase `Stock`.
- Eliminamos la declaración explícita de `_fields` porque el decorador se encargará de ello automáticamente.
- También eliminamos la llamada a `Stock.create_init()` porque el decorador se encarga de crear el método `__init__`.

Como resultado, la clase ahora es más simple y limpia. El decorador se encarga de todos los detalles que solíamos manejar manualmente.

6. Después de hacer estos cambios, necesitamos verificar que todo siga funcionando como se espera. Vuelve a ejecutar las pruebas usando los siguientes comandos:

```bash
cd ~/project
python3 teststock.py
```

Si todo está funcionando correctamente, deberías ver la siguiente salida:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Esta salida indica que todas las pruebas se han pasado con éxito.

También probemos nuestra clase `Stock` de forma interactiva. Ejecuta el siguiente comando en la terminal:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Deberías ver la siguiente salida:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

¡Genial! Has implementado con éxito un decorador de clase que simplifica nuestro código manejando automáticamente las declaraciones de campos e inicialización. Esto hace que nuestro código sea más eficiente y fácil de mantener.
