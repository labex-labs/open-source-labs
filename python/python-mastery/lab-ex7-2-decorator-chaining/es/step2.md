# Tu primer decorador con argumentos

El decorador `@logged` que definiste anteriormente siempre solo imprime un mensaje simple con el nombre de la función. Supongamos que quisieras que el usuario pudiera especificar un mensaje personalizado de algún tipo.

Define un nuevo decorador `@logformat(fmt)` que acepte una cadena de formato como argumento y use `fmt.format(func=func)` para formatear una función suministrada en un mensaje de registro:

```python
# sample.py
...
from logcall import logformat

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x,y):
    return x*y
```

Para hacer esto, debes definir un decorador que tome un argumento. Así es como debería verse cuando lo pruebas:

```python
>>> import sample
Adding logging to add
Adding logging to sub
Adding logging to mul
>>> sample.add(2,3)
Llamando a add
5
>>> sample.mul(2,3)
sample.py:mul
6
>>>
```

Para simplificar aún más el código, muestra cómo puedes definir el decorador original `@logged` usando el decorador `@logformat`.
