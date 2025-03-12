# Creando la clase Stock

En Python, una clase es un modelo (blueprint) para crear objetos. Te permite agrupar datos y funcionalidades juntos. Ahora, creemos nuestra clase `Stock` para representar información de acciones (stocks). Una acción tiene ciertas características, como su nombre, el número de acciones y el precio por acción. Definiremos atributos para estos aspectos dentro de nuestra clase.

1. Primero, debes estar en el directorio correcto en el WebIDE. Si no estás ya en el directorio `/home/labex/project`, navega hasta él. Aquí es donde trabajaremos en el código de nuestra clase `Stock`.

2. Una vez que estés en el directorio correcto, crea un nuevo archivo en el editor. Llama a este archivo `stock.py`. Este archivo contendrá el código de nuestra clase `Stock`.

3. Ahora, agreguemos el código para definir la clase `Stock`. Copia y pega el siguiente código en el archivo `stock.py`:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
```

En este código:

- La declaración `class Stock:` crea una nueva clase llamada `Stock`. Esto es como una plantilla para crear objetos de acciones.
- El método `__init__` es un método especial en las clases de Python. Se llama constructor. Cuando creas un nuevo objeto de la clase `Stock`, el método `__init__` se ejecutará automáticamente. Toma tres parámetros: `name`, `shares` y `price`. Estos parámetros representan la información sobre la acción.
- Dentro del método `__init__`, usamos `self` para referirnos a la instancia de la clase. Almacenamos los valores de los parámetros como atributos de instancia. Por ejemplo, `self.name = name` almacena el parámetro `name` como un atributo del objeto.
- El método `cost()` es un método personalizado que definimos. Calcula el costo total de la acción multiplicando el número de acciones (`self.shares`) por el precio por acción (`self.price`).

4. Después de agregar el código, guarda el archivo. Puedes hacerlo presionando `Ctrl+S` o haciendo clic en el icono de Guardar. Guardar el archivo asegura que tus cambios se conserven.

Examinemos el código nuevamente para asegurarnos de entenderlo:

- Definimos una clase llamada `Stock`. Esta clase se utilizará para crear objetos de acciones.
- El método `__init__` toma tres parámetros: `name`, `shares` y `price`. Inicializa los atributos del objeto con estos valores.
- Dentro de `__init__`, almacenamos estos parámetros como atributos de instancia usando `self`. Esto permite que cada objeto tenga su propio conjunto de valores para estos atributos.
- Agregamos un método `cost()` que calcula el costo total multiplicando el número de acciones por el precio. Esta es una funcionalidad útil para nuestros objetos de acciones.

Cuando creamos un objeto `Stock`, el método `__init__` se ejecutará automáticamente, configurando el estado inicial de nuestro objeto con los valores que proporcionamos. De esta manera, podemos crear fácilmente múltiples objetos de acciones con diferentes nombres, números de acciones y precios.
