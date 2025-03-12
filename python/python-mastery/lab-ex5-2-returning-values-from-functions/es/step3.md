# Trabajando con Futures para programación concurrente

En Python, cuando necesitas ejecutar funciones al mismo tiempo, es decir, de forma concurrente, el lenguaje ofrece herramientas útiles como hilos (threads) y procesos. Pero aquí está un problema común que enfrentarás: ¿cómo puedes obtener el valor que devuelve una función cuando se está ejecutando en un hilo diferente? Aquí es donde el concepto de un `Future` se vuelve muy importante.

Un `Future` es como un marcador de posición para un resultado que estará disponible más adelante. Es una forma de representar un valor que una función producirá en el futuro, incluso antes de que la función haya terminado de ejecutarse. Entendamos mejor este concepto con un ejemplo sencillo.

### Paso 1: Crear un nuevo archivo

Primero, necesitas crear un nuevo archivo de Python. Lo llamaremos `futures_demo.py`. Puedes usar el siguiente comando en tu terminal para crear este archivo:

```
touch ~/project/futures_demo.py
```

### Paso 2: Agregar código básico de la función

Ahora, abre el archivo `futures_demo.py` y agrega el siguiente código de Python. Este código define una función sencilla y muestra cómo funciona una llamada a función normal.

```python
import time
import threading
from concurrent.futures import Future, ThreadPoolExecutor

def worker(x, y):
    """A function that takes time to complete"""
    print('Starting work...')
    time.sleep(5)  # Simulate a time-consuming task
    print('Work completed')
    return x + y

# Part 1: Normal function call
print("--- Part 1: Normal function call ---")
result = worker(2, 3)
print(f"Result: {result}")
```

En este código, la función `worker` toma dos números, los suma, pero primero simula una tarea que consume tiempo deteniéndose durante 5 segundos. Cuando llamas a esta función de forma normal, el programa espera a que la función termine y luego obtiene el valor de retorno.

### Paso 3: Ejecutar el código básico

Guarda el archivo y ejecútalo usando el siguiente comando en tu terminal:

```
python ~/project/futures_demo.py
```

Deberías ver una salida como esta:

```
--- Part 1: Normal function call ---
Starting work...
Work completed
Result: 5
```

Esto muestra que una llamada a función normal espera a que la función termine y luego devuelve el resultado.

### Paso 4: Ejecutar la función en un hilo separado

A continuación, veamos qué sucede cuando ejecutamos la función `worker` en un hilo separado. Agrega el siguiente código al archivo `futures_demo.py`:

```python
# Part 2: Running in a separate thread (problem: no way to get result)
print("\n--- Part 2: Running in a separate thread ---")
t = threading.Thread(target=worker, args=(2, 3))
t.start()
print("Main thread continues while worker runs...")
t.join()  # Wait for the thread to complete
print("Worker thread finished, but we don't have its return value!")
```

Aquí, estamos usando la clase `threading.Thread` para iniciar la función `worker` en un nuevo hilo. El hilo principal no espera a que la función `worker` termine y continúa su ejecución. Sin embargo, cuando el hilo `worker` termina, no tenemos una forma fácil de obtener el valor de retorno.

### Paso 5: Ejecutar el código con hilos

Guarda el archivo nuevamente y ejecútalo usando el mismo comando:

```
python ~/project/futures_demo.py
```

Notarás que el hilo principal continúa, el hilo `worker` se ejecuta, pero no podemos acceder al valor de retorno de la función `worker`.

### Paso 6: Usar un `Future` manualmente

Para resolver el problema de obtener el valor de retorno de un hilo, podemos usar un objeto `Future`. Agrega el siguiente código al archivo `futures_demo.py`:

```python
# Part 3: Using a Future to get the result
print("\n--- Part 3: Using a Future manually ---")

def do_work_with_future(x, y, future):
    """Wrapper that sets the result in the Future"""
    result = worker(x, y)
    future.set_result(result)

# Create a Future object
fut = Future()

# Start a thread that will set the result in the Future
t = threading.Thread(target=do_work_with_future, args=(2, 3, fut))
t.start()

print("Main thread continues...")
print("Waiting for the result...")
# Block until the result is available
result = fut.result()  # This will wait until set_result is called
print(f"Got the result: {result}")
```

En este código, creamos un objeto `Future` y lo pasamos a una nueva función `do_work_with_future`. Esta función llama a la función `worker` y luego establece el resultado en el objeto `Future`. El hilo principal luego puede usar el método `result()` del objeto `Future` para obtener el resultado cuando esté disponible.

### Paso 7: Ejecutar el código con `Future`

Guarda el archivo y ejecútalo nuevamente:

```
python ~/project/futures_demo.py
```

Ahora verás que podemos obtener con éxito el valor de retorno de la función que se está ejecutando en el hilo.

### Paso 8: Usar `ThreadPoolExecutor`

La clase `ThreadPoolExecutor` en Python hace que trabajar con tareas concurrentes sea aún más fácil. Agrega el siguiente código al archivo `futures_demo.py`:

```python
# Part 4: Using ThreadPoolExecutor (easier way)
print("\n--- Part 4: Using ThreadPoolExecutor ---")
with ThreadPoolExecutor() as executor:
    # Submit the work to the executor
    future = executor.submit(worker, 2, 3)

    print("Main thread continues after submitting work...")
    print("Checking if the future is done:", future.done())

    # Get the result (will wait if not ready)
    result = future.result()
    print("Now the future is done:", future.done())
    print(f"Final result: {result}")
```

El `ThreadPoolExecutor` se encarga de crear y administrar los objetos `Future` por ti. Solo necesitas enviar la función y sus argumentos, y devolverá un objeto `Future` que puedes usar para obtener el resultado.

### Paso 9: Ejecutar el código completo

Guarda el archivo por última vez y ejecútalo:

```
python ~/project/futures_demo.py
```

### Explicación

1. **Llamada a función normal**: Cuando llamas a una función de forma normal, el programa espera a que la función termine y obtiene directamente el valor de retorno.
2. **Problema con los hilos**: Ejecutar una función en un hilo separado tiene una desventaja. No hay una forma incorporada de obtener el valor de retorno de la función que se está ejecutando en ese hilo.
3. **Future manual**: Al crear un objeto `Future` y pasarlo al hilo, podemos establecer el resultado en el `Future` y luego obtener el resultado desde el hilo principal.
4. **ThreadPoolExecutor**: Esta clase simplifica la programación concurrente. Se encarga de la creación y administración de los objetos `Future` por ti, lo que hace que sea más fácil ejecutar funciones de forma concurrente y obtener sus valores de retorno.

Los objetos `Future` tienen varios métodos útiles:

- `result()`: Este método se utiliza para obtener el resultado de la función. Si el resultado aún no está listo, esperará hasta que lo esté.
- `done()`: Puedes usar este método para comprobar si el cálculo de la función está completo.
- `add_done_callback()`: Este método te permite registrar una función que se llamará cuando el resultado esté listo.

Este patrón es muy importante en la programación concurrente, especialmente cuando necesitas obtener resultados de funciones que se ejecutan en paralelo.
