# Comprendiendo los conceptos básicos de exec()

En Python, la función `exec()` es una herramienta poderosa que te permite ejecutar código que se crea dinámicamente en tiempo de ejecución. Esto significa que puedes generar código sobre la marcha basado en cierta entrada o configuración, lo cual es extremadamente útil en muchos escenarios de programación.

Comencemos explorando el uso básico de la función `exec()`. Para hacer esto, abriremos una shell de Python. Abre tu terminal y escribe `python3`. Este comando iniciará el intérprete interactivo de Python, donde puedes ejecutar directamente código Python.

```bash
python3
```

Ahora, vamos a definir un fragmento de código Python como una cadena y luego usar la función `exec()` para ejecutarlo. Así es como funciona:

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
```

En este ejemplo:

1. Primero, definimos una cadena llamada `code`. Esta cadena contiene un bucle `for` de Python. El bucle está diseñado para iterar `n` veces y mostrar cada número de iteración.
2. Luego, definimos una variable `n` y le asignamos el valor 10. Esta variable se utiliza como límite superior para la función `range()` en nuestro bucle.
3. Después, llamamos a la función `exec()` con la cadena `code` como argumento. La función `exec()` toma la cadena y la ejecuta como código Python.
4. Finalmente, el bucle se ejecutó y mostró los números del 0 al 9.

El verdadero poder de la función `exec()` se vuelve más evidente cuando la usamos para crear estructuras de código más complejas, como funciones o métodos. Intentemos un ejemplo más avanzado donde crearemos dinámicamente un método `__init__()` para una clase.

```python
>>> class Stock:
...     _fields = ('name', 'shares', 'price')
...
>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
...     code += f'    self.{name} = {name}\n'
...
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # Now try the class
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
```

En este ejemplo más complejo:

1. Primero definimos una clase `Stock` con un atributo `_fields`. Este atributo es una tupla que contiene los nombres de los atributos de la clase.
2. Luego, creamos una cadena que representa código Python para un método `__init__`. Este método se utiliza para inicializar los atributos del objeto.
3. A continuación, usamos la función `exec()` para ejecutar la cadena de código. También pasamos un diccionario vacío `locs` a `exec()`. La función resultante de la ejecución se almacena en este diccionario.
4. Después, asignamos la función almacenada en el diccionario como el método `__init__` de nuestra clase `Stock`.
5. Finalmente, creamos una instancia de la clase `Stock` y verificamos que el método `__init__` funcione correctamente accediendo a los atributos del objeto.

Este ejemplo demuestra cómo se puede usar la función `exec()` para crear dinámicamente métodos basados en datos que están disponibles en tiempo de ejecución.
