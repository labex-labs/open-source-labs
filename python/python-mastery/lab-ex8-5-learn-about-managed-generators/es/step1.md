# Generadores como tareas

En un archivo `multitask.py`, defina el siguiente código:

```python
# multitask.py

from collections import deque

tasks = deque()
def run():
    while tasks:
        task = tasks.popleft()
        try:
            task.send(None)
            tasks.append(task)
        except StopIteration:
            print('Tarea terminada')
```

Este código implementa un pequeño planificador de tareas que ejecuta funciones generadoras. Pruebe ejecutándolo con las siguientes funciones.

```python
# multitask.py
...

def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1

def countup(n):
    x = 0
    while x < n:
        print('Vamos para arriba', x)
        yield
        x += 1

if __name__ == '__main__':
    tasks.append(countdown(10))
    tasks.append(countdown(5))
    tasks.append(countup(20))
    run()
```

Cuando ejecute esto, debería ver la salida de todos los generadores intercalada. Por ejemplo:

```python
T-minus 10
T-minus 5
Vamos para arriba 0
T-minus 9
T-minus 4
Vamos para arriba 1
T-minus 8
T-minus 3
Vamos para arriba 2
T-minus 7
T-minus 2
Vamos para arriba 3
T-minus 6
T-minus 1
Vamos para arriba 4
T-minus 5
Tarea terminada
Vamos para arriba 5
T-minus 4
Vamos para arriba 6
T-minus 3
Vamos para arriba 7
T-minus 2
Vamos para arriba 8
T-minus 1
Vamos para arriba 9
Tarea terminada
Vamos para arriba 10
Vamos para arriba 11
Vamos para arriba 12
Vamos para arriba 13
Vamos para arriba 14
Vamos para arriba 15
Vamos para arriba 16
Vamos para arriba 17
Vamos para arriba 18
Vamos para arriba 19
Tarea terminada
```

Eso es interesante, pero no especialmente convincente. Pase al siguiente ejemplo.
