# Adición de Validación de Argumentos de Métodos

En Python, validar datos es una parte importante para escribir código robusto. En esta sección, llevaremos nuestra validación un paso más allá validando automáticamente los argumentos de los métodos. El archivo `validate.py` ya incluye un decorador `@validated`. Un decorador en Python es una función especial que puede modificar otra función. El decorador `@validated` aquí puede verificar los argumentos de la función contra sus anotaciones. Las anotaciones en Python son una forma de agregar metadatos a los parámetros de la función y a los valores de retorno.

Modifiquemos nuestro código para aplicar este decorador a métodos con anotaciones:

1. Primero, necesitamos entender cómo funciona el decorador `validated`. Abra el archivo `validate.py` en su editor para revisarlo.

El decorador `validated` utiliza anotaciones de función para validar argumentos. Antes de permitir que la función se ejecute, crea una instancia de la clase validadora para cada parámetro anotado y llama al método `validate` para verificar el argumento. Por ejemplo, si un argumento está anotado con `PositiveInteger`, el decorador creará una instancia de `PositiveInteger` y validará que el valor pasado sea efectivamente un entero positivo. Si la validación falla, recopila todos los errores y lanza un `TypeError` con mensajes de error detallados.

2. Ahora, modificaremos la función `validate_attributes` en `structure.py` para envolver los métodos anotados con el decorador `validated`. Esto significa que cualquier método con anotaciones en la clase tendrá sus argumentos validados automáticamente. Abra el archivo `structure.py` en su editor.

3. Actualice la función `validate_attributes`:

```python
def validate_attributes(cls):
    """
    Class decorator that:
    1. Extracts Validator instances and builds _fields and _types lists
    2. Applies @validated decorator to methods with annotations
    """
    # Import the validated decorator
    from validate import validated

    # Process validator descriptors
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Apply @validated decorator to methods with annotations
    for name, val in vars(cls).items():
        if callable(val) and hasattr(val, '__annotations__'):
            setattr(cls, name, validated(val))

    # Create initialization method
    cls.create_init()

    return cls
```

Esta función actualizada ahora hace lo siguiente:

1. Procesa los descriptores de validación como antes. Los descriptores de validación se utilizan para definir reglas de validación para los atributos de clase.
2. Encuentra todos los métodos con anotaciones en la clase. Las anotaciones se agregan a los parámetros del método para especificar el tipo esperado del argumento.
3. Aplica el decorador `@validated` a esos métodos. Esto asegura que los argumentos pasados a estos métodos se validen de acuerdo con sus anotaciones.

4. Guarde el archivo después de realizar estos cambios. Guardar el archivo es importante porque asegura que nuestras modificaciones se almacenen y se puedan usar más adelante.

5. Ahora, actualicemos el método `sell` en la clase `Stock` para incluir una anotación. Las anotaciones ayudan a especificar el tipo esperado del argumento, que será utilizado por el decorador `@validated` para la validación. Abra el archivo `stock.py` en su editor.

6. Modifique el método `sell` para incluir una anotación de tipo:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

El cambio importante es agregar `: PositiveInteger` al parámetro `nshares`. Esto le dice a Python (y a nuestro decorador `@validated`) que valide este argumento usando el validador `PositiveInteger`. Por lo tanto, cuando llamemos al método `sell`, el argumento `nshares` debe ser un entero positivo.

7. Vuelva a ejecutar las pruebas para verificar que todo sigue funcionando. Ejecutar pruebas es una buena manera de asegurarse de que nuestros cambios no hayan roto ninguna funcionalidad existente.

```bash
cd ~/project
python3 teststock.py
```

Debería ver que todas las pruebas pasan:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

8. Probemos nuestra nueva validación de argumentos. Intentaremos llamar al método `sell` con argumentos válidos e inválidos para ver si la validación funciona como se espera.

```bash
cd ~/project
python3 -c "
from stock import Stock
s = Stock('GOOG', 100, 490.1)
s.sell(25)
print(s)
try:
    s.sell(-25)
except Exception as e:
    print(f'Error: {e}')
"
```

Debería ver una salida similar a:

```
Stock('GOOG', 75, 490.1)
Error: Bad Arguments
  nshares: nshares must be >= 0
```

¡Esto demuestra que nuestra validación de argumentos de métodos está funcionando! La primera llamada a `sell(25)` tiene éxito porque `25` es un entero positivo. Pero la segunda llamada a `sell(-25)` falla porque `-25` no es un entero positivo.

Ahora ha implementado un sistema completo para:

1. Validar atributos de clase usando descriptores. Los descriptores se utilizan para definir reglas de validación para los atributos de clase.
2. Recopilar automáticamente información de campos usando decoradores de clase. Los decoradores de clase pueden modificar el comportamiento de una clase, como la recopilación de información de campos.
3. Convertir datos de filas en instancias. Esto es útil cuando se trabaja con datos de fuentes externas.
4. Validar argumentos de métodos usando anotaciones. Las anotaciones ayudan a especificar el tipo esperado del argumento para la validación.

Esto demuestra el poder de combinar descriptores y decoradores en Python para crear clases expresivas y auto-validadoras.
