# Crear un objeto invocable básico

En Python, un objeto invocable (callable object) es un objeto que se puede usar como una función. Puedes pensar en él como algo que puedes "llamar" poniendo paréntesis después, similar a cómo se llama a una función normal. Para hacer que una clase en Python actúe como un objeto invocable, necesitamos implementar un método especial llamado `__call__`. Este método se invoca automáticamente cuando se usa el objeto con paréntesis, al igual que cuando se llama a una función.

Comencemos modificando el archivo `validate.py`. Vamos a agregar una nueva clase llamada `ValidatedFunction` a este archivo, y esta clase será nuestro objeto invocable. Para abrir el archivo en el editor de código, ejecuta el siguiente comando en la terminal:

```bash
code /home/labex/project/validate.py
```

Una vez que el archivo esté abierto, desplázate hasta el final y agrega el siguiente código:

```python
class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
```

Analicemos lo que hace este código. La clase `ValidatedFunction` tiene un método `__init__`, que es el constructor. Cuando se crea una instancia de esta clase, se le pasa una función. Esta función se almacena luego como un atributo de la instancia, llamado `self.func`.

El método `__call__` es la parte clave que hace que esta clase sea invocable. Cuando se llama a una instancia de la clase `ValidatedFunction`, se ejecuta este método `__call__`. Esto es lo que hace paso a paso:

1. Imprime un mensaje que indica qué función se está llamando. Esto es útil para depurar y entender lo que está sucediendo.
2. Llama a la función que se almacenó en `self.func` con los argumentos que se pasaron cuando se llamó a la instancia. Los `*args` y `**kwargs` permiten pasar cualquier número de argumentos posicionales y de palabra clave.
3. Devuelve el resultado de la llamada a la función.

Ahora, probemos esta clase `ValidatedFunction`. Crearemos un nuevo archivo llamado `test_callable.py` para escribir nuestro código de prueba. Para abrir este nuevo archivo en el editor de código, ejecuta el siguiente comando:

```bash
code /home/labex/project/test_callable.py
```

Agrega el siguiente código al archivo `test_callable.py`:

```python
from validate import ValidatedFunction

def add(x, y):
    return x + y

# Wrap the add function with ValidatedFunction
validated_add = ValidatedFunction(add)

# Call the wrapped function
result = validated_add(2, 3)
print(f"Result: {result}")

# Try another call
result = validated_add(10, 20)
print(f"Result: {result}")
```

En este código, primero importamos la clase `ValidatedFunction` del archivo `validate.py`. Luego definimos una función simple llamada `add` que toma dos números y devuelve su suma.

Creamos una instancia de la clase `ValidatedFunction`, pasándole la función `add`. Esto "envuelve" la función `add` dentro de la instancia de `ValidatedFunction`.

Luego llamamos a la función envuelta dos veces, una vez con los argumentos `2` y `3`, y luego con `10` y `20`. Cada vez que llamamos a la función envuelta, se invoca el método `__call__` de la clase `ValidatedFunction`, que a su vez llama a la función `add` original.

Para ejecutar el código de prueba, ejecuta el siguiente comando en la terminal:

```bash
python3 /home/labex/project/test_callable.py
```

Deberías ver una salida similar a esta:

```
Calling <function add at 0x7f2d1c3a9940>
Result: 5
Calling <function add at 0x7f2d1c3a9940>
Result: 30
```

Esta salida muestra que nuestro objeto invocable está funcionando como se espera. Cuando llamamos a `validated_add(2, 3)`, en realidad estamos llamando al método `__call__` de la clase `ValidatedFunction`, que luego llama a la función `add` original.

Por ahora, nuestra clase `ValidatedFunction` solo imprime un mensaje y pasa la llamada a la función original. En el siguiente paso, mejoraremos esta clase para realizar validación de tipo basada en las anotaciones de la función.
