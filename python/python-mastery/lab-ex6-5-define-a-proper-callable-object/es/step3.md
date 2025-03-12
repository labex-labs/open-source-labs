# Implementar validación de tipos con anotaciones de funciones

En Python, tienes la capacidad de agregar anotaciones de tipo a los parámetros de una función. Estas anotaciones sirven como una forma de indicar los tipos de datos esperados de los parámetros y el valor de retorno de una función. Por defecto, no imponen los tipos en tiempo de ejecución, pero se pueden utilizar con fines de validación.

Echemos un vistazo a un ejemplo:

```python
def add(x: int, y: int) -> int:
    return x + y
```

En este código, `x: int` y `y: int` nos indican que los parámetros `x` e `y` deben ser enteros. El `-> int` al final indica que la función `add` devuelve un entero. Estas anotaciones de tipo se almacenan en el atributo `__annotations__` de la función, que es un diccionario que mapea los nombres de los parámetros a sus tipos anotados.

Ahora, vamos a mejorar nuestra clase `ValidatedFunction` para utilizar estas anotaciones de tipo para la validación. Para hacer esto, necesitaremos utilizar el módulo `inspect` de Python. Este módulo proporciona funciones útiles para obtener información sobre objetos en tiempo de ejecución, como módulos, clases, métodos, funciones, etc. En nuestro caso, lo utilizaremos para hacer coincidir los argumentos de la función con sus nombres de parámetros correspondientes.

Primero, necesitamos modificar la clase `ValidatedFunction` en el archivo `validate.py`. Puedes abrir este archivo utilizando el siguiente comando:

```bash
code /home/labex/project/validate.py
```

Reemplaza la clase `ValidatedFunction` existente con la siguiente versión mejorada:

```python
import inspect

class ValidatedFunction:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __call__(self, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(*args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(*args, **kwargs)
```

Esto es lo que hace esta versión mejorada:

1. Utiliza `inspect.signature()` para obtener información sobre los parámetros de la función, como sus nombres, valores predeterminados y tipos anotados.
2. El método `bind()` de la firma se utiliza para hacer coincidir los argumentos proporcionados con sus nombres de parámetros correspondientes. Esto nos ayuda a asociar cada argumento con su parámetro correcto en la función.
3. Comprueba cada argumento contra su anotación de tipo (si existe). Si se encuentra una anotación, recupera la clase de validación de la anotación y aplica la validación utilizando el método `check()`.
4. Finalmente, llama a la función original con los argumentos validados.

Ahora, probemos esta clase `ValidatedFunction` mejorada con algunas funciones que utilizan nuestras clases de validación en sus anotaciones de tipo. Abre el archivo `test_validation.py` utilizando el siguiente comando:

```bash
code /home/labex/project/test_validation.py
```

Agrega el siguiente código al archivo:

```python
from validate import ValidatedFunction, Integer, String

def greet(name: String, times: Integer):
    return name * times

# Wrap the greet function with ValidatedFunction
validated_greet = ValidatedFunction(greet)

# Valid call
try:
    result = validated_greet("Hello ", 3)
    print(f"Valid call result: {result}")
except TypeError as e:
    print(f"Unexpected error: {e}")

# Invalid call - wrong type for 'name'
try:
    result = validated_greet(123, 3)
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for name: {e}")

# Invalid call - wrong type for 'times'
try:
    result = validated_greet("Hello ", "3")
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for times: {e}")
```

En este código, definimos una función `greet` con anotaciones de tipo `name: String` y `times: Integer`. Esto significa que el parámetro `name` debe ser validado utilizando la clase `String`, y el parámetro `times` debe ser validado utilizando la clase `Integer`. Luego envuelvemos la función `greet` con nuestra clase `ValidatedFunction` para habilitar la validación de tipos.

Realizamos tres casos de prueba: una llamada válida, una llamada inválida con el tipo incorrecto para `name` y una llamada inválida con el tipo incorrecto para `times`. Cada llamada está envuelta en un bloque `try-except` para capturar cualquier excepción `TypeError` que se pueda generar durante la validación.

Para ejecutar el archivo de prueba, utiliza el siguiente comando:

```bash
python3 /home/labex/project/test_validation.py
```

Deberías ver una salida similar a la siguiente:

```
Valid call result: Hello Hello Hello
Expected error for name: Expected <class 'str'>
Expected error for times: Expected <class 'int'>
```

Esta salida demuestra que nuestro objeto invocable `ValidatedFunction` ahora está aplicando la validación de tipos basada en las anotaciones de la función. Cuando pasamos argumentos del tipo incorrecto, las clases de validación detectan el error y generan una excepción `TypeError`. De esta manera, podemos asegurarnos de que las funciones se llamen con los tipos de datos correctos, lo que ayuda a prevenir errores y hace que nuestro código sea más robusto.
