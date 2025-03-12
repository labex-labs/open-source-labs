# Creación de decoradores con argumentos

Hasta ahora, hemos estado utilizando el decorador `@logged`, que siempre imprime un mensaje fijo. Pero, ¿qué pasa si quieres personalizar el formato del mensaje? En esta sección, aprenderemos cómo crear un nuevo decorador que pueda aceptar argumentos, lo que te dará más flexibilidad en cómo utilizas los decoradores.

## Comprendiendo los decoradores parametrizados

Un decorador parametrizado es un tipo especial de función. En lugar de modificar directamente otra función, devuelve un decorador. La estructura general de un decorador parametrizado es la siguiente:

```python
def decorator_with_args(arg1, arg2, ...):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use arg1, arg2, ... here
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator
```

Cuando se utiliza `@decorator_with_args(value1, value2)` en tu código, Python primero llama a `decorator_with_args(value1, value2)`. Esta llamada devuelve el decorador real, que luego se aplica a la función que sigue la sintaxis `@`. Este proceso de dos pasos es clave en cómo funcionan los decoradores parametrizados.

## Creando el decorador logformat

Vamos a crear un decorador `@logformat(fmt)` que tome una cadena de formato como argumento. Esto nos permitirá personalizar el mensaje de registro.

1. Abre `logcall.py` en el WebIDE y agrega el nuevo decorador. El código siguiente muestra cómo definir tanto el decorador `logged` existente como el nuevo decorador `logformat`:

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

En el decorador `logformat`, la función exterior `logformat` toma una cadena de formato `fmt` como argumento. Luego devuelve la función `decorator`, que es el decorador real que modifica la función objetivo.

2. Ahora, probemos nuestro nuevo decorador modificando `sample.py`. El siguiente código muestra cómo usar tanto el decorador `logged` como el decorador `logformat` en diferentes funciones:

```python
from logcall import logged, logformat

@logged
def add(x, y):
    "Adds two numbers"
    return x + y

@logged
def sub(x, y):
    "Subtracts y from x"
    return x - y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
    "Multiplies two numbers"
    return x * y
```

Aquí, las funciones `add` y `sub` utilizan el decorador `logged`, mientras que la función `mul` utiliza el decorador `logformat` con una cadena de formato personalizada.

3. Ejecuta el archivo `sample.py` actualizado para ver los resultados. Abre tu terminal y ejecuta el siguiente comando:

```bash
cd ~/project
python3 -c "import sample; print(sample.add(2, 3)); print(sample.mul(2, 3))"
```

Deberías ver una salida similar a la siguiente:

```
Calling add
5
sample.py:mul
6
```

Esta salida muestra que el decorador `logged` imprime el nombre de la función como se esperaba, y el decorador `logformat` utiliza la cadena de formato personalizada para imprimir el nombre del archivo y el nombre de la función.

## Redefiniendo el decorador logged utilizando logformat

Ahora que tenemos un decorador `logformat` más flexible, podemos redefinir nuestro decorador `logged` original utilizando este. Esto nos ayudará a reutilizar código y mantener un formato de registro consistente.

1. Actualiza `logcall.py` con el siguiente código:

```python
from functools import wraps

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Define logged using logformat
logged = lambda func: logformat("Calling {func.__name__}")(func)
```

Aquí, utilizamos una función lambda para definir el decorador `logged` en términos del decorador `logformat`. La función lambda toma una función `func` y aplica el decorador `logformat` con una cadena de formato específica.

2. Prueba que el decorador `logged` redefinido sigue funcionando. Abre tu terminal y ejecuta el siguiente comando:

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def greet(name):
    return f'Hello, {name}'
    
print(greet('World'))"
```

Deberías ver:

```
Calling greet
Hello, World
```

Esto muestra que el decorador `logged` redefinido funciona como se esperaba, y hemos reutilizado con éxito el decorador `logformat` para lograr un formato de registro consistente.
