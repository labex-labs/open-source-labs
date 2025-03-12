# Probando nuestro programador de tareas (task scheduler)

Ahora, vamos a agregar una prueba a nuestro archivo `multitask.py`. El propósito de esta prueba es ejecutar múltiples tareas al mismo tiempo, lo que se conoce como ejecución concurrente. La ejecución concurrente permite que diferentes tareas avancen al parecer al mismo tiempo, aunque en un entorno de un solo hilo (single - threaded), las tareas en realidad se turnan para ejecutarse.

Para realizar esta prueba, agrega el siguiente código al final del archivo `multitask.py`:

```python
# Test our scheduler
if __name__ == '__main__':
    # Add tasks to the queue
    tasks.append(countdown(10))  # Count down from 10
    tasks.append(countdown(5))   # Count down from 5
    tasks.append(countup(20))    # Count up to 20

    # Run all tasks
    run()
```

En este código, primero verificamos si el script se está ejecutando directamente usando `if __name__ == '__main__':`. Luego, agregamos tres tareas diferentes a la cola `tasks`. Las tareas `countdown` contarán hacia atrás desde los números dados, y la tarea `countup` contará hacia arriba hasta el número especificado. Finalmente, llamamos a la función `run()` para comenzar a ejecutar estas tareas.

Después de agregar el código, ejecútalo con el siguiente comando en la terminal:

```bash
python3 /home/labex/project/multitask.py
```

Cuando ejecutes el código, deberías ver una salida similar a esta (el orden exacto de las líneas puede variar):

```
T-minus 10
T-minus 5
Up we go 0
T-minus 9
T-minus 4
Up we go 1
T-minus 8
T-minus 3
Up we go 2
...
```

Observa cómo la salida de las diferentes tareas está mezclada. Esto es una clara indicación de que nuestro programador de tareas está ejecutando las tres tareas de forma concurrente. Cada vez que una tarea alcanza una declaración `yield`, el programador de tareas pausa esa tarea y cambia a otra, lo que permite que todas las tareas avancen con el tiempo.

## Cómo funciona

Echemos un vistazo más de cerca a lo que sucede cuando nuestro programador de tareas se ejecuta:

1. Primero, agregamos tres tareas generadoras a la cola: `countdown(10)`, `countdown(5)` y `countup(20)`. Estas tareas generadoras son funciones especiales que pueden pausar y reanudar su ejecución en las declaraciones `yield`.
2. Luego, la función `run()` comienza a trabajar:
   - Toma la primera tarea, `countdown(10)`, de la cola.
   - Ejecuta esta tarea hasta que alcanza una declaración `yield`. Cuando llega al `yield`, imprime "T-minus 10".
   - Después de eso, agrega la tarea `countdown(10)` de nuevo a la cola para que se pueda ejecutar de nuevo más tarde.
   - A continuación, toma la tarea `countdown(5)` de la cola.
   - Ejecuta la tarea `countdown(5)` hasta que alcanza una declaración `yield`, imprimiendo "T-minus 5".
   - Y este proceso continúa...

Este ciclo continúa hasta que todas las tareas se completan. Cada tarea tiene la oportunidad de ejecutarse durante un corto tiempo, lo que da la ilusión de ejecución concurrente sin necesidad de usar hilos (threads) o callbacks. Los hilos son una forma más compleja de lograr concurrencia, y los callbacks se utilizan en la programación asíncrona. Nuestro sencillo programador de tareas utiliza generadores para lograr un efecto similar de manera más sencilla.
