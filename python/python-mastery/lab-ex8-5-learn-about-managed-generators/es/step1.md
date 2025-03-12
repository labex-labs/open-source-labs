# Comprendiendo los generadores de Python

Comencemos revisando qué son los generadores en Python. En Python, los generadores son un tipo especial de función. Son diferentes de las funciones regulares. Cuando se llama a una función regular, se ejecuta desde el principio hasta el final y devuelve un solo valor. Sin embargo, una función generadora devuelve un iterador, que es un objeto a través del cual podemos iterar, lo que significa que podemos acceder a sus valores uno por uno.

Los generadores utilizan la declaración `yield` para devolver valores. En lugar de devolver todos los valores a la vez como una función regular, un generador devuelve valores uno a la vez. Después de devolver un valor, el generador suspende su ejecución. La próxima vez que solicitamos un valor, reanuda la ejecución desde donde se detuvo.

## Creando un generador sencillo

Ahora, creemos un generador sencillo. En el WebIDE, debes crear un nuevo archivo. Este archivo contendrá el código de nuestro generador. Nombrar el archivo `generator_demo.py` y colocarlo en el directorio `/home/labex/project`. Aquí está el contenido que debes poner en el archivo:

```python
# Generator function that counts down from n
def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Countdown complete!")

# Create a generator object
counter = countdown(5)

# Drive the generator manually
print(next(counter))  # 5
print(next(counter))  # 4
print(next(counter))  # 3

# Iterate through remaining values
for value in counter:
    print(value)  # 2, 1
```

En este código, primero definimos una función generadora llamada `countdown`. Esta función toma un número `n` como argumento y cuenta hacia atrás desde `n` hasta 1. Dentro de la función, usamos un bucle `while` para decrementar `n` y devolver cada valor. Cuando llamamos a `countdown(5)`, crea un objeto generador llamado `counter`.

Luego usamos la función `next()` para obtener manualmente valores del generador. Cada vez que llamamos a `next(counter)`, el generador reanuda la ejecución desde donde se detuvo y devuelve el siguiente valor. Después de obtener manualmente tres valores, usamos un bucle `for` para iterar a través de los valores restantes en el generador.

Para ejecutar este código, abre la terminal y ejecuta el siguiente comando:

```bash
python3 /home/labex/project/generator_demo.py
```

Cuando ejecutes el código, deberías ver la siguiente salida:

```
Starting countdown from 5
5
4
3
2
1
Countdown complete!
```

Veamos cómo se comporta la función generadora:

1. La función generadora comienza su ejecución cuando llamamos por primera vez a `next(counter)`. Antes de eso, la función solo está definida y no se ha comenzado a contar hacia atrás realmente.
2. Se detiene en cada declaración `yield`. Después de devolver un valor, se detiene y espera la siguiente llamada a `next()`.
3. Cuando llamamos a `next()` de nuevo, continúa desde donde se detuvo. Por ejemplo, después de devolver 5, recuerda el estado y continúa decrementando `n` y devolviendo el siguiente valor.
4. La función generadora completa su ejecución después de devolver el último valor. En nuestro caso, después de devolver 1, imprime "Countdown complete!".

Esta capacidad de pausar y reanudar la ejecución es lo que hace a los generadores poderosos. Es muy útil para tareas como la programación de tareas (task scheduling) y la programación asíncrona, donde necesitamos realizar múltiples tareas de manera eficiente sin bloquear la ejecución de otras tareas.
