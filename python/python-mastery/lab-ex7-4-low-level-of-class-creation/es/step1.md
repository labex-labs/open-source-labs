# Creación manual de clases

En la programación en Python, las clases son un concepto fundamental que te permite agrupar datos y funciones. Por lo general, definimos clases utilizando la sintaxis estándar de Python. Por ejemplo, aquí está una simple clase `Stock`. Esta clase representa una acción con atributos como `name`, `shares` y `price`, y tiene métodos para calcular el costo y vender acciones.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Pero, ¿alguna vez te has preguntado cómo Python realmente crea una clase detrás de escena? ¿Qué pasaría si quisiéramos crear esta clase sin utilizar la sintaxis estándar de clases? En esta sección, exploraremos cómo se construyen las clases de Python a un nivel más bajo.

## Lanzar la shell interactiva de Python

Para comenzar a experimentar con la creación manual de clases, necesitamos abrir una shell interactiva de Python. Esta shell nos permite ejecutar código Python línea por línea, lo cual es excelente para aprender y probar.

Abre una terminal en WebIDE y comienza la shell interactiva de Python escribiendo los siguientes comandos. El primer comando `cd ~/project` cambia el directorio actual al directorio del proyecto, y el segundo comando `python3` inicia la shell interactiva de Python 3.

```bash
cd ~/project
python3
```

## Definir métodos como funciones regulares

Antes de crear una clase manualmente, necesitamos definir los métodos que formarán parte de la clase. En Python, los métodos son simplemente funciones asociadas a una clase. Entonces, definamos los métodos que queremos en nuestra clase como funciones regulares de Python.

```python
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

def sell(self, nshares):
    self.shares -= nshares
```

Aquí, la función `__init__` es un método especial en las clases de Python. Se llama constructor y se utiliza para inicializar los atributos del objeto cuando se crea una instancia de la clase. El método `cost` calcula el costo total de las acciones, y el método `sell` reduce el número de acciones.

## Crear un diccionario de métodos

Ahora que hemos definido nuestros métodos como funciones regulares, necesitamos organizarlos de una manera que Python pueda entender al crear la clase. Lo hacemos creando un diccionario que contendrá todos los métodos de nuestra clase.

```python
methods = {
    '__init__': __init__,
    'cost': cost,
    'sell': sell
}
```

En este diccionario, las claves son los nombres de los métodos tal como se utilizarán en la clase, y los valores son los objetos de función reales que definimos anteriormente.

## Utilizar el constructor type() para crear una clase

En Python, la función `type()` es una función incorporada que se puede utilizar para crear clases a un nivel más bajo. La función `type()` toma tres argumentos:

1. El nombre de la clase: Esta es una cadena que representa el nombre de la clase que queremos crear.
2. Una tupla de clases base: En Python, las clases pueden heredar de otras clases. Aquí, usamos `(object,)` lo que significa que nuestra clase hereda de la clase base `object`, que es la clase base de todas las clases en Python.
3. Un diccionario que contiene métodos y atributos: Este es el diccionario que creamos anteriormente que contiene todos los métodos de nuestra clase.

```python
Stock = type('Stock', (object,), methods)
```

Esta línea de código crea una nueva clase llamada `Stock` utilizando la función `type()`. La clase hereda de la clase `object` y tiene los métodos definidos en el diccionario `methods`.

## Probar nuestra clase creada manualmente

Ahora que hemos creado nuestra clase manualmente, probémosla para asegurarnos de que funcione como se espera. Crearemos una instancia de nuestra nueva clase y llamaremos a sus métodos.

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
s.sell(25)
print(s.shares)
```

En la primera línea, creamos una instancia de la clase `Stock` con el nombre `GOOG`, 100 acciones y un precio de 490.10. Luego imprimimos el nombre de la acción, calculamos e imprimimos el costo, vendemos 25 acciones y, finalmente, imprimimos el número de acciones restantes.

Deberías ver la siguiente salida:

```
GOOG
49010.0
75
```

Esta salida muestra que nuestra clase creada manualmente funciona igual que una clase creada utilizando la sintaxis estándar de Python. Demuestra que una clase es fundamentalmente solo un nombre, una tupla de clases base y un diccionario de métodos y atributos. La función `type()` simplemente construye un objeto de clase a partir de estos componentes.

Sal de la shell de Python cuando hayas terminado:

```python
exit()
```
