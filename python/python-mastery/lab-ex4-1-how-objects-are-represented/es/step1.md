# Creación de una clase simple de acciones

En este paso, vamos a crear una clase simple para representar una acción (stock). Comprender cómo crear clases es fundamental en Python, ya que nos permite modelar objetos del mundo real y sus comportamientos. Esta clase simple de acciones será nuestro punto de partida para explorar cómo funcionan internamente los objetos de Python.

Para comenzar, necesitamos abrir una shell interactiva de Python. La shell interactiva de Python es un excelente lugar para experimentar con código Python. Puedes escribir y ejecutar comandos de Python uno por uno. Para abrirla, escribe el siguiente comando en la terminal:

```bash
python3
```

Una vez que hayas ingresado el comando, verás el indicador de Python (`>>>`). Esto indica que ahora estás dentro de la shell interactiva de Python y puedes comenzar a escribir código Python.

Ahora, definamos una clase `SimpleStock`. Una clase en Python es como un plano para crear objetos. Define los atributos (datos) y métodos (funciones) que tendrán los objetos de esa clase. Así es como se define la clase `SimpleStock` con los atributos y métodos necesarios:

```python
>>> class SimpleStock:
...     def __init__(self, name, shares, price):
...         self.name = name
...         self.shares = shares
...         self.price = price
...     def cost(self):
...         return self.shares * self.price
...
```

En el código anterior, el método `__init__` es un método especial en las clases de Python. Se llama constructor y se utiliza para inicializar los atributos del objeto cuando se crea un objeto. El parámetro `self` se refiere a la instancia de la clase que se está creando. El método `cost` calcula el costo total de las acciones multiplicando el número de acciones por el precio por acción.

Después de definir la clase, podemos crear instancias de la clase `SimpleStock`. Una instancia es un objeto real creado a partir del plano de la clase. Creemos dos instancias para representar diferentes acciones:

```python
>>> goog = SimpleStock('GOOG', 100, 490.10)
>>> ibm = SimpleStock('IBM', 50, 91.23)
```

Estas instancias representan 100 acciones de Google a $490.10 por acción y 50 acciones de IBM a $91.23 por acción. Cada instancia tiene su propio conjunto de valores de atributos.

Verifiquemos que nuestras instancias estén funcionando correctamente. Podemos hacer esto comprobando sus atributos y calculando su costo. Esto nos ayudará a confirmar que la clase y sus métodos están funcionando como se espera.

```python
>>> goog.name
'GOOG'
>>> goog.shares
100
>>> goog.price
490.1
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
```

El método `cost()` multiplica el número de acciones por el precio por acción para calcular el costo total de poseer esas acciones. Al ejecutar estos comandos, podemos ver que las instancias tienen los valores de atributos correctos y que el método `cost` está calculando el costo con precisión.
