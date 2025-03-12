# Construyendo un decorador de validación

En este paso, vamos a crear un decorador más práctico. Un decorador en Python es un tipo especial de función que puede modificar el comportamiento de otra función. El decorador que crearemos validará los argumentos de una función basándose en las anotaciones de tipo. Las anotaciones de tipo son una forma de especificar los tipos de datos esperados de los argumentos y el valor de retorno de una función. Este es un caso de uso común en aplicaciones del mundo real, ya que ayuda a garantizar que las funciones reciban los tipos de entrada correctos, lo que puede prevenir muchos errores.

## Entendiendo las clases de validación

Ya hemos creado un archivo llamado `validate.py` para ti, y contiene algunas clases de validación. Las clases de validación se utilizan para comprobar si un valor cumple con ciertos criterios. Para ver lo que hay dentro de este archivo, debes abrirlo en el editor VSCode. Puedes hacer esto ejecutando los siguientes comandos en la terminal:

```bash
cd /home/labex/project
code validate.py
```

El archivo tiene tres clases:

1. `Validator` - Esta es una clase base. Una clase base proporciona un marco general o estructura que otras clases pueden heredar. En este caso, proporciona la estructura básica para la validación.
2. `Integer` - Esta clase de validador se utiliza para asegurarse de que un valor es un entero. Si pasas un valor que no es entero a una función que utiliza este validador, se generará un error.
3. `PositiveInteger` - Esta clase de validador asegura que un valor es un entero positivo. Entonces, si pasas un entero negativo o cero, también se generará un error.

## Agregando el decorador de validación

Ahora, vamos a agregar una función decorador llamada `validated` al archivo `validate.py`. Este decorador realizará varias tareas importantes:

1. Inspeccionará las anotaciones de tipo de una función. Las anotaciones de tipo son como notas pequeñas que nos dicen qué tipo de datos espera la función.
2. Validará los argumentos pasados a la función en contra de estas anotaciones de tipo. Esto significa que comprobará si los valores pasados a la función son del tipo correcto.
3. También validará el valor de retorno de la función en contra de su anotación. Entonces, se asegura de que la función devuelva el tipo de datos que se supone que debe devolver.
4. Si la validación falla, generará mensajes de error informativos. Estos mensajes te dirán exactamente qué salió mal, como qué argumento tenía el tipo incorrecto.

Agrega el siguiente código al final del archivo `validate.py`:

```python
# Add to validate.py

import inspect
import functools

def validated(func):
    sig = inspect.signature(func)

    print(f'Validating {func.__name__} {sig}')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Bind arguments to the signature
        bound = sig.bind(*args, **kwargs)
        errors = []

        # Validate each argument
        for name, value in bound.arguments.items():
            if name in sig.parameters:
                param = sig.parameters[name]
                if param.annotation != inspect.Parameter.empty:
                    try:
                        # Create an instance of the validator and validate the value
                        if isinstance(param.annotation, type) and issubclass(param.annotation, Validator):
                            validator = param.annotation()
                            bound.arguments[name] = validator.validate(value)
                    except Exception as e:
                        errors.append(f'    {name}: {e}')

        # If validation errors, raise an exception
        if errors:
            raise TypeError('Bad Arguments\n' + '\n'.join(errors))

        # Call the function
        result = func(*bound.args, **bound.kwargs)

        # Validate the return value
        if sig.return_annotation != inspect.Signature.empty:
            try:
                if isinstance(sig.return_annotation, type) and issubclass(sig.return_annotation, Validator):
                    validator = sig.return_annotation()
                    result = validator.validate(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}') from None

        return result

    return wrapper
```

Este código utiliza el módulo `inspect` de Python. El módulo `inspect` nos permite obtener información sobre objetos en tiempo de ejecución, como funciones. Aquí, lo usamos para examinar la firma de la función y validar los argumentos basados en las anotaciones de tipo. También usamos `functools.wraps`. Esta es una función auxiliar que preserva los metadatos de la función original, como su nombre y docstring. Los metadatos son como información adicional sobre la función que nos ayuda a entender lo que hace.

## Probando el decorador de validación

Vamos a crear un archivo para probar nuestro decorador de validación. Crearemos un nuevo archivo llamado `test_validate.py` y agregaremos el siguiente código a él:

```python
# test_validate.py

from validate import Integer, PositiveInteger, validated

@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x ** y

# Test with a class
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Ahora, probaremos nuestro decorador en el intérprete de Python. Primero, navega al directorio del proyecto y inicia el intérprete de Python ejecutando estos comandos en la terminal:

```bash
cd /home/labex/project
python3
```

Luego, en el intérprete de Python, podemos ejecutar el siguiente código para probar nuestro decorador:

```python
>>> from test_validate import add, pow, Stock
Validating add (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating pow (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating sell (self, nshares: validate.PositiveInteger) -> <class 'inspect._empty'>
>>>
>>> # Test with valid inputs
>>> add(2, 3)
5
>>>
>>> # Test with invalid inputs
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>
>>>
>>> # Test valid power
>>> pow(2, 3)
8
>>>
>>> # Test with negative exponent (produces non - integer result)
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
>>> # Test with a class
>>> s = Stock("GOOG", 100, 490.1)
>>> s.sell(50)
>>> s.shares
50
>>>
>>> # Test with invalid shares
>>> s.sell(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    nshares: Expected value > 0
>>> exit()
```

Como puedes ver, nuestro decorador `validated` ha aplicado con éxito la comprobación de tipos en los argumentos y valores de retorno de las funciones. Esto es muy útil porque hace que nuestro código sea más robusto. En lugar de dejar que los errores de tipo se propaguen más profundo en el código y causen errores difíciles de encontrar, los capturamos en los límites de las funciones.
