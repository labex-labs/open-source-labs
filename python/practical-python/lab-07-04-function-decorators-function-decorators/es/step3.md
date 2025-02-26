# Código que agrega registro

Quizás puedas crear una función que agregue registro a otras funciones. Un envoltorio.

```python
def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Ahora úsalo.

```python
def add(x, y):
    return x + y

logged_add = logged(add)
```

¿Qué pasa cuando llamas a la función devuelta por `logged`?

```python
logged_add(3, 4)      # Verás que aparece el mensaje de registro
```

Este ejemplo ilustra el proceso de creación de una llamada _función envoltorio_.

Un envoltorio es una función que se encierra alrededor de otra función con un poco de procesamiento adicional, pero de otra manera funciona exactamente de la misma manera que la función original.

```python
>>> logged_add(3, 4)
Llamando a add   # Salida adicional. Agregada por el envoltorio
7
>>>
```

_Nota: La función `logged()` crea el envoltorio y lo devuelve como resultado._
