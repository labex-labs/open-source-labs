# Comprobar propiedad

Crea una función llamada `check_prop` que tome dos parámetros: `fn` y `prop`. El parámetro `fn` es una función predicado que se aplicará a la propiedad especificada de un diccionario. El parámetro `prop` es una cadena que representa el nombre de la propiedad a la que se aplicará la función predicado.

La función `check_prop` debe devolver una función lambda que tome un diccionario y aplique la función predicado, `fn`, a la propiedad especificada.

```python
def check_prop(fn, prop):
  return lambda obj: fn(obj[prop])
```

```python
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```
