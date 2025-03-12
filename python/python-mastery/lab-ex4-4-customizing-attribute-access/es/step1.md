# Comprendiendo `__setattr__` para el control de atributos

En Python, hay métodos especiales que te permiten personalizar cómo se accede y se modifican los atributos de un objeto. Uno de estos métodos importantes es `__setattr__()`. Este método entra en juego cada vez que intentas asignar un valor a un atributo de un objeto. Te da la capacidad de tener un control detallado sobre el proceso de asignación de atributos.

## ¿Qué es `__setattr__`?

El método `__setattr__(self, name, value)` actúa como un interceptor para todas las asignaciones de atributos. Cuando escribes una simple declaración de asignación como `obj.attr = value`, Python no asigna directamente el valor. En lugar de eso, llama internamente a `obj.__setattr__("attr", value)`. Este mecanismo te brinda el poder de decidir qué debe suceder durante la asignación de atributos.

Veamos ahora un ejemplo práctico de cómo podemos usar `__setattr__` para restringir qué atributos se pueden establecer en una clase.

### Paso 1: Crear un nuevo archivo

Primero, abre un nuevo archivo en el WebIDE. Puedes hacer esto haciendo clic en el menú "File" y luego seleccionando "New File". Nombrar este archivo `restricted_stock.py` y guardarlo en el directorio `/home/labex/project`. Este archivo contendrá la definición de la clase donde usaremos `__setattr__` para controlar la asignación de atributos.

### Paso 2: Agregar código a `restricted_stock.py`

Agrega el siguiente código al archivo `restricted_stock.py`. Este código define una clase `RestrictedStock`.

```python
class RestrictedStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __setattr__(self, name, value):
        # Only allow specific attributes
        if name not in {'name', 'shares', 'price'}:
            raise AttributeError(f'Cannot set attribute {name}')

        # If attribute is allowed, set it using the parent method
        super().__setattr__(name, value)
```

En el método `__init__`, inicializamos el objeto con los atributos `name`, `shares` y `price`. El método `__setattr__` comprueba si el nombre del atributo que se está asignando está en el conjunto de atributos permitidos (`name`, `shares`, `price`). Si no lo está, levanta un `AttributeError`. Si el atributo está permitido, utiliza el método `__setattr__` de la clase padre para establecer realmente el atributo.

### Paso 3: Crear un archivo de prueba

Crea un nuevo archivo llamado `test_restricted.py` y agrega el siguiente código a él. Este código probará la funcionalidad de la clase `RestrictedStock`.

```python
from restricted_stock import RestrictedStock

# Create a new stock
stock = RestrictedStock('GOOG', 100, 490.1)

# Test accessing existing attributes
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")

# Test modifying an existing attribute
print("\nChanging shares to 75...")
stock.shares = 75
print(f"New shares value: {stock.shares}")

# Test setting an invalid attribute
try:
    print("\nTrying to set an invalid attribute 'share'...")
    stock.share = 50
except AttributeError as e:
    print(f"Error: {e}")
```

En este código, primero importamos la clase `RestrictedStock`. Luego creamos una instancia de la clase. Probamos el acceso a atributos existentes, la modificación de un atributo existente y, finalmente, intentamos establecer un atributo no válido para ver si el método `__setattr__` funciona como se espera.

### Paso 4: Ejecutar el archivo de prueba

Abre una terminal en el WebIDE y ejecuta los siguientes comandos para ejecutar el archivo `test_restricted.py`:

```bash
cd /home/labex/project
python3 test_restricted.py
```

Después de ejecutar estos comandos, deberías ver una salida similar a esta:

```
Name: GOOG
Shares: 100
Price: 490.1

Changing shares to 75...
New shares value: 75

Trying to set an invalid attribute 'share'...
Error: Cannot set attribute share
```

## Cómo funciona

El método `__setattr__` en nuestra clase `RestrictedStock` funciona en los siguientes pasos:

1. Primero comprueba si el nombre del atributo está en el conjunto permitido (`name`, `shares`, `price`).
2. Si el nombre del atributo no está en el conjunto permitido, levanta un `AttributeError`. Esto evita la asignación de atributos no deseados.
3. Si el atributo está permitido, utiliza `super().__setattr__()` para establecer realmente el atributo. Esto asegura que el proceso normal de asignación de atributos se lleve a cabo para los atributos permitidos.

Este método es más flexible que usar `__slots__`, que vimos en ejemplos anteriores. Si bien `__slots__` puede optimizar el uso de memoria y restringir atributos, tiene limitaciones cuando se trabaja con herencia y puede entrar en conflicto con otras características de Python. Nuestro enfoque con `__setattr__` nos da un control similar sobre la asignación de atributos sin algunas de esas limitaciones.
