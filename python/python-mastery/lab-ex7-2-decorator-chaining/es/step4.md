# Validación (Redux)

En el último ejercicio, escribiste un decorador `@validated` que enforce las anotaciones de tipo. Por ejemplo:

```python
@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y
```

Crea un nuevo decorador `@enforce()` que enfoque los tipos especificados a través de argumentos de palabras clave al decorador en lugar de eso. Por ejemplo:

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

El comportamiento resultante de la función decorada debe ser idéntico. Nota: Haz que la palabra clave `return_` especifique el tipo de retorno. `return` es una palabra reservada de Python, por lo que tienes que elegir un nombre ligeramente diferente.

**Discusión**

Escribir decoradores robustos a menudo es mucho más difícil de lo que parece. Lectura recomendada:
