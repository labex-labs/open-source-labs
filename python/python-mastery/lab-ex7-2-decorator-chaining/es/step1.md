# Preservación de metadatos de funciones en decoradores

En Python, los decoradores son una herramienta poderosa que te permite modificar el comportamiento de las funciones. Sin embargo, cuando se utiliza un decorador para envolver una función, surge un pequeño problema. Por defecto, los metadatos de la función original, como su nombre, la cadena de documentación (docstring) y las anotaciones, se pierden. Los metadatos son importantes porque ayudan en la introspección (examinar la estructura del código) y en la generación de documentación. Primero, verificaremos este problema.

Abre tu terminal en el WebIDE. Ejecutaremos algunos comandos de Python para ver lo que sucede cuando se utiliza un decorador. Los siguientes comandos crearán una función simple `add` envuelta con un decorador y luego imprimirán la función y su docstring.

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

Cuando ejecutes estos comandos, verás una salida similar a esta:

```
<function wrapper at 0x...>
None
```

Observa que en lugar de mostrar el nombre de la función como `add`, muestra `wrapper`. Y la docstring, que debería ser `'Adds two things'`, es `None`. Esto puede ser un gran problema cuando se utilizan herramientas que dependen de estos metadatos, como herramientas de introspección o generadores de documentación.

## Solucionando el problema con functools.wraps

El módulo `functools` de Python viene al rescate. Proporciona un decorador `wraps` que puede ayudarnos a preservar los metadatos de la función. Veamos cómo podemos modificar nuestro decorador `logged` para usar `wraps`.

1. Primero, abre el archivo `logcall.py` en el WebIDE. Puedes navegar al directorio del proyecto utilizando el siguiente comando en la terminal:

```bash
cd ~/project
```

2. Ahora, actualiza el decorador `logged` en `logcall.py` con el siguiente código. El decorador `@wraps(func)` es la clave aquí. Copia todos los metadatos de la función original `func` a la función envolvente.

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

3. El decorador `@wraps(func)` realiza un trabajo importante. Toma todos los metadatos (como el nombre, la docstring y las anotaciones) de la función original `func` y los adjunta a la función `wrapper`. De esta manera, cuando usamos la función decorada, tendrá los metadatos correctos.

4. Probemos nuestro decorador mejorado. Ejecuta los siguientes comandos en la terminal:

```bash
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

Ahora deberías ver:

```
<function add at 0x...>
Adds two things
```

¡Genial! El nombre de la función y la docstring se han preservado. Esto significa que nuestro decorador ahora está funcionando como se esperaba y los metadatos de la función original están intactos.

## Solucionando el decorador validate.py

Ahora, apliquemos la misma solución al decorador `validated` en `validate.py`. Este decorador se utiliza para validar los tipos de los argumentos de la función y el valor de retorno en función de las anotaciones de la función.

1. Abre `validate.py` en el WebIDE.

2. Actualiza el decorador `validated` con el decorador `@wraps`. El siguiente código muestra cómo hacerlo. El decorador `@wraps(func)` se agrega a la función `wrapper` dentro del decorador `validated` para preservar los metadatos.

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
```

3. Probemos que nuestro decorador `validated` ahora preserva los metadatos. Ejecuta los siguientes comandos en la terminal:

```bash
python3 -c "from validate import validated, Integer; @validated
def multiply(x: Integer, y: Integer) -> Integer:
    'Multiplies two integers'
    return x * y
    
print(multiply)
print(multiply.__doc__)"
```

Deberías ver:

```
<function multiply at 0......>
Multiplies two integers
```

Ahora, ambos decoradores, `logged` y `validated`, preservan adecuadamente los metadatos de las funciones que decoran. Esto asegura que cuando se utilizan estos decoradores, las funciones seguirán teniendo sus nombres, docstrings y anotaciones originales, lo cual es muy útil para la legibilidad y el mantenimiento del código.
