# Componer funciones

## Problema

Escribe una función llamada `compose(*fns)` que acepte una o más funciones como argumentos y devuelva una nueva función que es el resultado de la composición de las funciones de entrada de derecha a izquierda. La última (más a la derecha) función puede aceptar uno o más argumentos; el resto de las funciones deben ser unarias.

## Ejemplo

```python
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```

En el ejemplo anterior, definimos dos funciones `add5` y `multiply`. Luego utilizamos la función `compose()` para crear una nueva función llamada `multiply_and_add_5` que primero multiplica sus dos argumentos y luego suma 5 al resultado. Cuando llamamos a `multiply_and_add_5(5, 2)`, obtenemos el resultado `15`.
