# Usar `yield from` en corutinas

En este paso, exploraremos cómo usar la declaración `yield from` con corutinas para aplicaciones más prácticas. Las corutinas son un concepto poderoso en Python, y entender cómo usar `yield from` con ellas puede simplificar en gran medida tu código.

## Corutinas y paso de mensajes

Las corutinas son funciones especiales que pueden recibir valores a través de la declaración `yield`. Son increíblemente útiles para tareas como el procesamiento de datos y el manejo de eventos. En el archivo `cofollow.py`, hay un decorador `consumer`. Este decorador ayuda a configurar las corutinas avanzándolas automáticamente hasta el primer punto `yield`. Esto significa que no tienes que iniciar manualmente la corutina; el decorador se encarga de ello por ti.

Vamos a crear una corutina que reciba valores y valide su tipo. Así es como puedes hacerlo:

1. Primero, abre el archivo `cofollow.py` en el editor. Puedes usar el siguiente comando en la terminal para navegar al directorio correcto:

```bash
cd /home/labex/project
```

2. A continuación, agrega la siguiente función `receive` al final del archivo `cofollow.py`. Esta función es una corutina que recibirá un mensaje y validará su tipo.

```python
def receive(expected_type):
    """
    A coroutine that receives a message and validates its type.
    Returns the received message if it matches the expected type.
    """
    msg = yield
    assert isinstance(msg, expected_type), f'Expected type {expected_type}'
    return msg
```

Esto es lo que hace esta función:

- Utiliza `yield` sin una expresión para recibir un valor. Cuando se envía un valor a la corutina, esta declaración `yield` lo capturará.
- Comprueba si el valor recibido es del tipo esperado utilizando la función `isinstance`. Si el tipo no coincide, genera un `AssertionError`.
- Si la comprobación de tipo es exitosa, devuelve el valor.

3. Ahora, vamos a crear una corutina que use `yield from` con nuestra función `receive`. Esta nueva corutina recibirá e imprimirá solo enteros.

```python
@consumer
def print_ints():
    """
    A coroutine that receives and prints integers only.
    Uses yield from to delegate to the receive coroutine.
    """
    while True:
        val = yield from receive(int)
        print('Got:', val)
```

4. Para probar esta corutina, abre una shell de Python y ejecuta el siguiente código:

```python
from cofollow import print_ints

p = print_ints()
p.send(42)
p.send(13)
try:
    p.send('13')  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

Deberías ver la siguiente salida:

```
Got: 42
Got: 13
Error: Expected type <class 'int'>
```

## Comprender cómo funciona `yield from` con corutinas

Cuando usamos `yield from receive(int)` en la corutina `print_ints`, ocurren los siguientes pasos:

1. El control se delega a la corutina `receive`. Esto significa que la corutina `print_ints` se pausa y la corutina `receive` comienza a ejecutarse.
2. La corutina `receive` utiliza `yield` para recibir un valor. Espera a que se le envíe un valor.
3. Cuando se envía un valor a `print_ints`, en realidad lo recibe `receive`. La declaración `yield from` se encarga de pasar el valor de `print_ints` a `receive`.
4. La corutina `receive` valida el tipo del valor recibido. Si el tipo es correcto, devuelve el valor.
5. El valor devuelto se convierte en el resultado de la expresión `yield from` en la corutina `print_ints`. Esto significa que la variable `val` en `print_ints` se le asigna el valor devuelto por `receive`.

Usar `yield from` hace que el código sea más legible que si tuviéramos que manejar el devolver y recibir valores directamente. Abstrae la complejidad del paso de valores entre corutinas.

## Crear corutinas de comprobación de tipos más avanzadas

Vamos a expandir nuestras funciones de utilidad para manejar validaciones de tipo más complejas. Así es como puedes hacerlo:

1. Agrega las siguientes funciones al archivo `cofollow.py`:

```python
def receive_dict():
    """Receive and validate a dictionary"""
    result = yield from receive(dict)
    return result

def receive_str():
    """Receive and validate a string"""
    result = yield from receive(str)
    return result

@consumer
def process_data():
    """Process different types of data using the receive utilities"""
    while True:
        print("Waiting for a string...")
        name = yield from receive_str()
        print(f"Got string: {name}")

        print("Waiting for a dictionary...")
        data = yield from receive_dict()
        print(f"Got dictionary with {len(data)} items: {data}")

        print("Processing complete for this round.")
```

2. Para probar la nueva corutina, abre una shell de Python y ejecuta el siguiente código:

```python
from cofollow import process_data

proc = process_data()
proc.send("John Doe")
proc.send({"age": 30, "city": "New York"})
proc.send("Jane Smith")
try:
    proc.send(123)  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

Deberías ver una salida como esta:

```
Waiting for a string...
Got string: John Doe
Waiting for a dictionary...
Got dictionary with 2 items: {'age': 30, 'city': 'New York'}
Processing complete for this round.
Waiting for a string...
Got string: Jane Smith
Waiting for a dictionary...
Error: Expected type <class 'dict'>
```

La declaración `yield from` hace que el código sea más limpio y legible. Nos permite centrarnos en la lógica de alto nivel de nuestro programa en lugar de perdernos en los detalles del paso de mensajes entre corutinas.
