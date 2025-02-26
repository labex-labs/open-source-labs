# Tu primer decorador

Para comenzar con los decoradores, escribe una función decoradora _muy_ simple que simplemente imprima un mensaje cada vez que se llama a una función. Crea un archivo `logcall.py` y define la siguiente función:

```python
# logcall.py

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Ahora, crea un archivo separado `sample.py` y aplícala a algunas definiciones de función:

```python
# sample.py

from logcall import logged

@logged
def add(x,y):
    return x+y

@logged
def sub(x,y):
    return x-y
```

Prueba tu código de la siguiente manera:

```python
>>> import sample
Adding logging to add
Adding logging to sub
>>> sample.add(3,4)
Calling add
7
>>> sample.sub(2,3)
Calling sub
-1
>>>
```
