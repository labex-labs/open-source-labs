# Creando un programador de tareas (task scheduler) con generadores

En programación, un programador de tareas (task scheduler) es una herramienta crucial que ayuda a gestionar y ejecutar múltiples tareas de manera eficiente. En esta sección, usaremos generadores para construir un sencillo programador de tareas que pueda ejecutar múltiples funciones generadoras de forma concurrente. Esto te mostrará cómo se pueden gestionar los generadores para realizar multitarea cooperativa, lo que significa que las tareas se turnan para ejecutarse y comparten el tiempo de ejecución.

Primero, debes crear un nuevo archivo. Navega al directorio `/home/labex/project` y crea un archivo llamado `multitask.py`. Este archivo contendrá el código de nuestro programador de tareas.

```python
# multitask.py

from collections import deque

# Task queue
tasks = deque()

# Simple task scheduler
def run():
    while tasks:
        task = tasks.popleft()  # Get the next task
        try:
            task.send(None)     # Resume the task
            tasks.append(task)  # Put it back in the queue
        except StopIteration:
            print('Task done')  # Task is complete

# Example task 1: Countdown
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield              # Pause execution
        n -= 1

# Example task 2: Count up
def countup(n):
    x = 0
    while x < n:
        print('Up we go', x)
        yield              # Pause execution
        x += 1
```

Ahora, analicemos cómo funciona este programador de tareas:

1. Usamos un `deque` (cola doblemente terminada) para almacenar nuestras tareas generadoras. Un `deque` es una estructura de datos que te permite agregar y eliminar elementos de ambos extremos de manera eficiente. Es una excelente opción para nuestra cola de tareas porque necesitamos agregar tareas al final y eliminarlas del frente.
2. La función `run()` es el corazón de nuestro programador de tareas. Toma las tareas de la cola una por una:
   - Reanuda cada tarea usando `send(None)`. Esto es similar a usar `next()` en un generador. Le dice al generador que continúe la ejecución desde donde se detuvo.
   - Después de que la tarea devuelva un valor (yield), se agrega de nuevo al final de la cola. De esta manera, la tarea tendrá otra oportunidad de ejecutarse más tarde.
   - Cuando una tarea se completa (lanza `StopIteration`), se elimina de la cola. Esto indica que la tarea ha terminado su ejecución.
3. Cada declaración `yield` en nuestras tareas generadoras actúa como un punto de pausa. Cuando un generador alcanza una declaración `yield`, pausa su ejecución y devuelve el control al programador de tareas. Esto permite que otras tareas se ejecuten.

Este enfoque implementa la multitarea cooperativa. Cada tarea cede voluntariamente el control al programador de tareas, lo que permite que otras tareas se ejecuten. De esta manera, múltiples tareas pueden compartir el tiempo de ejecución y ejecutarse de forma concurrente.
