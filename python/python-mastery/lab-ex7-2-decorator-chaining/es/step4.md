# Creación de un decorador de aplicación de tipos con argumentos

En los pasos anteriores, aprendimos sobre el decorador `@validated`. Este decorador se utiliza para aplicar las anotaciones de tipo en las funciones de Python. Las anotaciones de tipo son una forma de especificar los tipos esperados de los argumentos de una función y de sus valores de retorno. Ahora, vamos a ir un paso más allá. Crearemos un decorador más flexible que pueda aceptar especificaciones de tipo como argumentos. Esto significa que podemos definir los tipos que queremos para cada argumento y el valor de retorno de una manera más explícita.

## Comprendiendo el objetivo

Nuestro objetivo es crear un decorador `@enforce()`. Este decorador nos permitirá especificar restricciones de tipo utilizando argumentos de palabra clave. Aquí tienes un ejemplo de cómo funcionará:

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

En este ejemplo, estamos utilizando el decorador `@enforce` para especificar que los argumentos `x` e `y` de la función `add` deben ser de tipo `Integer`, y el valor de retorno también debe ser de tipo `Integer`. Este decorador se comportará de manera similar al decorador `@validated` anterior, pero nos da más control sobre las especificaciones de tipo.

## Creando el decorador enforce

1. Primero, abre el archivo `validate.py` en el WebIDE. Agregaremos nuestro nuevo decorador a este archivo. Aquí está el código que agregaremos:

```python
from functools import wraps

class Integer:
    @classmethod
    def __instancecheck__(cls, x):
        return isinstance(x, int)

def validated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get function annotations
        annotations = func.__annotations__
        # Check arguments against annotations
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            if arg_name in annotations and not isinstance(arg_value, annotations[arg_name]):
                raise TypeError(f'Expected {arg_name} to be {annotations[arg_name].__name__}')

        # Run the function and get the result
        result = func(*args, **kwargs)

        # Check the return value
        if 'return' in annotations and not isinstance(result, annotations['return']):
            raise TypeError(f'Expected return value to be {annotations["return"].__name__}')

        return result
    return wrapper

def enforce(**type_specs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check argument types
            for arg_name, arg_value in zip(func.__code__.co_varnames, args):
                if arg_name in type_specs and not isinstance(arg_value, type_specs[arg_name]):
                    raise TypeError(f'Expected {arg_name} to be {type_specs[arg_name].__name__}')

            # Run the function and get the result
            result = func(*args, **kwargs)

            # Check the return value
            if 'return_' in type_specs and not isinstance(result, type_specs['return_']):
                raise TypeError(f'Expected return value to be {type_specs["return_"].__name__}')

            return result
        return wrapper
    return decorator
```

Analicemos lo que hace este código. La clase `Integer` se utiliza para definir un tipo personalizado. El decorador `validated` comprueba los tipos de los argumentos de la función y el valor de retorno en función de las anotaciones de tipo de la función. El decorador `enforce` es el nuevo que estamos creando. Toma argumentos de palabra clave que especifican los tipos para cada argumento y el valor de retorno. Dentro de la función `wrapper` del decorador `enforce`, comprobamos si los tipos de los argumentos y el valor de retorno coinciden con los tipos especificados. Si no, lanzamos una excepción `TypeError`.

2. Ahora, probemos nuestro nuevo decorador `@enforce`. Ejecutaremos algunos casos de prueba para ver si funciona como se espera. Aquí está el código para ejecutar las pruebas:

```bash
cd ~/project
python3 -c "from validate import enforce, Integer

@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y

# This should work
print(add(2, 3))

# This should raise a TypeError
try:
    print(add('2', 3))
except TypeError as e:
    print(f'Error: {e}')

# This should raise a TypeError
try:
    @enforce(x=Integer, y=Integer, return_=Integer)
    def bad_add(x, y):
        return str(x + y)
    print(bad_add(2, 3))
except TypeError as e:
    print(f'Error: {e}')"
```

En este código de prueba, primero definimos una función `add` con el decorador `@enforce`. Luego llamamos a la función `add` con argumentos válidos, lo que debería funcionar sin errores. A continuación, llamamos a la función `add` con un argumento no válido, lo que debería lanzar una excepción `TypeError`. Finalmente, definimos una función `bad_add` que devuelve un valor del tipo incorrecto, lo que también debería lanzar una excepción `TypeError`.

Cuando ejecutes este código de prueba, deberías ver una salida similar a la siguiente:

```
5
Error: Expected x to be Integer
Error: Expected return value to be Integer
```

Esta salida muestra que nuestro decorador `@enforce` está funcionando correctamente. Lanza una excepción `TypeError` cuando los tipos de los argumentos o el valor de retorno no coinciden con los tipos especificados.

## Comparando los dos enfoques

Tanto el decorador `@validated` como el decorador `@enforce` logran el mismo objetivo de aplicar restricciones de tipo, pero lo hacen de diferentes maneras.

1. El decorador `@validated` utiliza las anotaciones de tipo integradas de Python. Aquí tienes un ejemplo:

   ```python
   @validated
   def add(x: Integer, y: Integer) -> Integer:
       return x + y
   ```

   Con este enfoque, especificamos los tipos directamente en la definición de la función utilizando anotaciones de tipo. Esta es una característica integrada de Python y proporciona mejor soporte en Entornos de Desarrollo Integrados (IDEs). Los IDEs pueden utilizar estas anotaciones de tipo para proporcionar finalización de código, comprobación de tipos y otras características útiles.

2. El decorador `@enforce`, por otro lado, utiliza argumentos de palabra clave para especificar los tipos. Aquí tienes un ejemplo:

   ```python
   @enforce(x=Integer, y=Integer, return_=Integer)
   def add(x, y):
       return x + y
   ```

   Este enfoque es más explícito porque estamos pasando directamente las especificaciones de tipo como argumentos al decorador. Puede ser útil cuando se trabaja con bibliotecas que se basan en otros sistemas de anotación.

Cada enfoque tiene sus propias ventajas. Las anotaciones de tipo son una parte nativa de Python y ofrecen mejor soporte en los IDE, mientras que el enfoque `@enforce` nos da más flexibilidad y explicación. Puedes elegir el enfoque que mejor se adapte a tus necesidades según el proyecto en el que estés trabajando.
