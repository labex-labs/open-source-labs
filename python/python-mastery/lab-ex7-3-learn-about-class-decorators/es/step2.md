# Creación de un Decorador de Clases para Validación

En el paso anterior, nuestra implementación funcionó, pero había una redundancia. Teníamos que especificar tanto la tupla `_fields` como los atributos de descriptor. Esto no es muy eficiente y podemos mejorarlo. En Python, los decoradores de clases son una herramienta potente que puede ayudarnos a simplificar este proceso. Un decorador de clases es una función que toma una clase como argumento, la modifica de alguna manera y luego devuelve la clase modificada. Al usar un decorador de clases, podemos extraer automáticamente la información de los campos de los descriptores, lo que hará que nuestro código sea más limpio y mantenible.

Creemos un decorador de clases para simplificar nuestro código. Aquí están los pasos que debe seguir:

1. Primero, abra el archivo `structure.py` en su editor.

2. A continuación, agregue el siguiente código en la parte superior del archivo `structure.py`, justo después de cualquier declaración de importación. Este código define nuestro decorador de clases:

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
- Finalmente, llama al método `create_init()` de la clase para generar el método `__init__`, y luego devuelve la clase modificada.

3. Una vez que haya agregado el código, guarde el archivo `structure.py`. Guardar el archivo asegura que sus cambios se conserven.

4. Ahora, necesitamos modificar nuestro archivo `stock.py` para usar este nuevo decorador. Abra el archivo `stock.py` en su editor.

5. Actualice el archivo `stock.py` para usar el decorador `validate_attributes`. Reemplace el código existente con el siguiente:

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

Observe los cambios que hemos realizado:

- Agregamos el decorador `@validate_attributes` justo encima de la definición de la clase `Stock`. Esto le indica a Python que aplique el decorador `validate_attributes` a la clase `Stock`.
- Eliminamos la declaración explícita de `_fields` porque el decorador se encargará de ello automáticamente.
- También eliminamos la llamada a `Stock.create_init()` porque el decorador se encarga de crear el método `__init__`.

Como resultado, la clase ahora es más simple y limpia. El decorador se encarga de todos los detalles que solíamos manejar manualmente.

6. Después de realizar estos cambios, debemos verificar que todo siga funcionando como se esperaba. Ejecute las pruebas nuevamente usando los siguientes comandos:

```bash
cd ~/project
python3 teststock.py
```

Si todo funciona correctamente, debería ver la siguiente salida:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Esta salida indica que todas las pruebas han pasado con éxito.

Probemos también nuestra clase `Stock` de forma interactiva. Ejecute el siguiente comando en la terminal:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Debería ver la siguiente salida:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

¡Genial! Ha implementado con éxito un decorador de clases que simplifica nuestro código al manejar automáticamente las declaraciones de campos y la inicialización. Esto hace que nuestro código sea más eficiente y fácil de mantener.
