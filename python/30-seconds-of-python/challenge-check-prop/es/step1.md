# Comprobar propiedad

## Problema

Crea una función llamada `check_prop` que tome dos parámetros: `fn` y `prop`. El parámetro `fn` es una función predicado que se aplicará a la propiedad especificada de un diccionario. El parámetro `prop` es una cadena que representa el nombre de la propiedad a la que se aplicará la función predicado.

La función `check_prop` debe devolver una función lambda que tome un diccionario y aplique la función predicado, `fn`, a la propiedad especificada.

## Ejemplo

```python
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```

En el ejemplo anterior, creamos una función `check_age` que comprueba si el valor de la propiedad `age` en un diccionario es mayor o igual a 18. Luego creamos un diccionario `user` con una propiedad `name` y `age`. Finalmente, llamamos a la función `check_age` con el diccionario `user` como argumento, lo que devuelve `True` ya que la propiedad `age` es igual a 18.
