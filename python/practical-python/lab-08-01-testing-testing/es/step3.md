# Pruebas en línea

Las aserciones también se pueden utilizar para pruebas simples.

```python
def add(x, y):
    return x + y

assert add(2,2) == 4
```

De esta manera, se incluye la prueba en el mismo módulo que el código.

_Ventaja: Si el código está obviamente roto, las intentos de importar el módulo se detendrán con un error._

No se recomienda utilizar esto para pruebas exhaustivas. Es más una "prueba de humo" básica. ¿Funciona la función con cualquier ejemplo? Si no, entonces algo está definitivamente roto.
