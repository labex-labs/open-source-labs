# Funciones personalizadas

Utilice funciones para el código que desee reutilizar. Aquí hay una definición de función:

```python
def sumcount(n):
    '''
    Devuelve la suma de los primeros n enteros
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total
```

Para llamar a una función.

```python
a = sumcount(100)
```

Una función es una serie de instrucciones que realizan una tarea y devuelven un resultado. La palabra clave `return` es necesaria para especificar explícitamente el valor de retorno de la función.
