# Mejorando la clase Stock

En Python, las clases son una forma poderosa de organizar datos y comportamiento. Nos permiten agrupar datos y funciones relacionados. En esta sección, mejoraremos nuestra clase `Stock` agregando un método que muestre la información de las acciones formateada. Este es un gran ejemplo de cómo podemos encapsular tanto datos como comportamiento en nuestras clases. La encapsulación significa agrupar datos con los métodos que operan sobre esos datos, lo que ayuda a mantener nuestro código organizado y más fácil de gestionar.

1. Primero, necesitas abrir el archivo `stock.py` en el editor del WebIDE. El archivo `stock.py` es donde hemos estado trabajando en nuestra clase `Stock`. Abrirlo en el editor nos permite hacer cambios en la definición de la clase.

2. Ahora, modificaremos la clase `Stock` para agregar un nuevo método `display()`. Este método se encargará de imprimir la información de las acciones de manera bien formateada. Así es como puedes hacerlo:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def display(self):
        print(f"Stock: {self.name}, Shares: {self.shares}, Price: ${self.price:.2f}, Total Cost: ${self.cost():.2f}")
```

En el método `__init__`, inicializamos el nombre de la acción, el número de acciones y el precio. El método `cost` calcula el costo total de la acción multiplicando el número de acciones por el precio. El nuevo método `display` utiliza una f - cadena para formatear e imprimir la información de la acción, incluyendo el nombre, el número de acciones, el precio y el costo total.

3. Después de hacer estos cambios, necesitas guardar el archivo. Puedes hacerlo presionando `Ctrl+S` en tu teclado o haciendo clic en el icono de Guardar en el editor. Guardar el archivo asegura que tus cambios se conserven y se puedan utilizar más tarde.

4. A continuación, iniciaremos una nueva sesión interactiva de Python. Una sesión interactiva nos permite probar nuestro código inmediatamente. Para iniciar la sesión, ejecuta el siguiente comando en la terminal:

```bash
python3 -i stock.py
```

La opción `-i` le dice a Python que inicie una sesión interactiva después de ejecutar el archivo `stock.py`. De esta manera, podemos usar la clase `Stock` y sus métodos de inmediato.

5. Ahora, creemos un objeto de acción y usemos el nuevo método `display()`. Crearemos un objeto que represente las acciones de Apple y luego llamaremos al método `display` para ver la información formateada. Aquí está el código:

```python
apple = Stock('AAPL', 200, 154.50)
apple.display()
```

Cuando ejecutes este código en la sesión interactiva, verás la siguiente salida:

```
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

Esta salida muestra que el método `display` está funcionando correctamente y está formateando la información de la acción como se esperaba.

6. Finalmente, creemos una lista de acciones y mostrémoslas todas. Esto mostrará cómo podemos usar el método `display` con múltiples objetos de acciones. Aquí está el código:

```python
stocks = [
    Stock('GOOG', 100, 490.10),
    Stock('IBM', 50, 91.50),
    Stock('AAPL', 200, 154.50)
]

for stock in stocks:
    stock.display()
```

Cuando ejecutes este código, obtendrás la siguiente salida:

```
Stock: GOOG, Shares: 100, Price: $490.10, Total Cost: $49010.00
Stock: IBM, Shares: 50, Price: $91.50, Total Cost: $4575.00
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

Al agregar el método `display()` a nuestra clase, hemos encapsulado la lógica de formato dentro de la clase misma. Esto hace que nuestro código sea más organizado y más fácil de mantener. Si necesitamos cambiar la forma en que se muestra la información de las acciones, solo necesitamos modificar el método `display` en un solo lugar, en lugar de hacer cambios en todo nuestro código.
