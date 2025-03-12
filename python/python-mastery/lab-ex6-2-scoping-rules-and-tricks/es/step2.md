# Usar `locals()` para acceder a los argumentos de una función

En Python, comprender los ámbitos de las variables es crucial. El ámbito de una variable determina en qué parte del código se puede acceder a ella. Python proporciona una función incorporada llamada `locals()` que es muy útil para que los principiantes comprendan el ámbito. La función `locals()` devuelve un diccionario que contiene todas las variables locales en el ámbito actual. Esto puede ser extremadamente útil cuando se desea inspeccionar los argumentos de una función, ya que ofrece una vista clara de qué variables están disponibles en una parte específica del código.

Creemos un experimento sencillo en el intérprete de Python para ver cómo funciona esto. Primero, necesitamos navegar al directorio del proyecto e iniciar el intérprete de Python. Puedes hacer esto ejecutando los siguientes comandos en tu terminal:

```bash
cd ~/project
python3
```

Una vez que estés en la shell interactiva de Python, definiremos una clase `Stock`. Una clase en Python es como un modelo para crear objetos. En esta clase, usaremos el método especial `__init__`. El método `__init__` es un constructor en Python, lo que significa que se llama automáticamente cuando se crea un objeto de la clase. Dentro de este método `__init__`, usaremos la función `locals()` para imprimir todas las variables locales.

```python
class Stock:
    def __init__(self, name, shares, price):
        print(locals())
```

Ahora, creemos una instancia de esta clase `Stock`. Una instancia es un objeto real creado a partir del modelo de la clase. Pasaremos algunos valores para los parámetros `name`, `shares` y `price`.

```python
s = Stock('GOOG', 100, 490.1)
```

Cuando ejecutes este código, deberías ver una salida similar a:

```
{'self': <__main__.Stock object at 0x...>, 'name': 'GOOG', 'shares': 100, 'price': 490.1}
```

Esta salida muestra que `locals()` nos da un diccionario que contiene todas las variables locales en el método `__init__`. La referencia `self` es una variable especial en las clases de Python que se refiere a la instancia de la clase misma. Las otras variables son los valores de los parámetros que pasamos al crear el objeto `Stock`.

Podemos usar esta funcionalidad de `locals()` para inicializar automáticamente los atributos de un objeto. Los atributos son variables asociadas con un objeto. Definamos una función auxiliar y modifiquemos nuestra clase `Stock`.

```python
def _init(locs):
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)

class Stock:
    def __init__(self, name, shares, price):
        _init(locals())
```

La función `_init` toma el diccionario de variables locales obtenido de `locals()`. Primero, elimina la referencia `self` del diccionario usando el método `pop`. Luego, itera sobre los pares clave - valor restantes en el diccionario y usa la función `setattr` para establecer cada variable como un atributo en el objeto.

Ahora, probemos esta implementación con argumentos posicionales y de palabra clave. Los argumentos posicionales se pasan en el orden en que se definen en la firma de la función, mientras que los argumentos de palabra clave se pasan con los nombres de los parámetros especificados.

```python
# Test with positional arguments
s1 = Stock('GOOG', 100, 490.1)
print(s1.name, s1.shares, s1.price)

# Test with keyword arguments
s2 = Stock(name='AAPL', shares=50, price=125.3)
print(s2.name, s2.shares, s2.price)
```

¡Ambos enfoques deberían funcionar ahora! La función `_init` nos permite manejar tanto los argumentos posicionales como los de palabra clave sin problemas. También conserva los nombres de los parámetros en la firma de la función, lo que hace que la salida de `help()` sea más útil. La función `help()` en Python proporciona información sobre funciones, clases y módulos, y tener intactos los nombres de los parámetros hace que esta información sea más significativa.

Cuando hayas terminado de experimentar, puedes salir del intérprete de Python ejecutando el siguiente comando:

```python
exit()
```
