# Comprender el protocolo de descriptores

En este paso, vamos a aprender cómo funcionan los descriptores en Python creando una simple clase `Stock`. Los descriptores en Python son una característica poderosa que te permite personalizar cómo se accede, se establece y se elimina un atributo. El protocolo de descriptores consiste en tres métodos especiales: `__get__()`, `__set__()` y `__delete__()`. Estos métodos definen cómo se comporta el descriptor cuando se accede a un atributo, se le asigna un valor o se elimina, respectivamente.

Primero, necesitamos crear un nuevo archivo llamado `stock.py` en el directorio del proyecto. Este archivo contendrá nuestra clase `Stock`. Aquí está el código que debes poner en el archivo `stock.py`:

```python
# stock.py

class Stock:
    __slots__ = ['_name', '_shares', '_price']

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._price = value

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

En esta clase `Stock`, estamos usando el decorador `property` para definir métodos getter y setter para los atributos `name`, `shares` y `price`. Estos métodos getter y setter actúan como descriptores, lo que significa que controlan cómo se accede y se establecen estos atributos. Por ejemplo, los métodos setter validan los valores de entrada para asegurarse de que son del tipo correcto y dentro de un rango aceptable.

Ahora que tenemos nuestro archivo `stock.py` listo, abramos una shell de Python para experimentar con la clase `Stock` y ver cómo funcionan los descriptores en acción. Para hacer esto, abre tu terminal y ejecuta los siguientes comandos:

```bash
cd ~/project
python3 -i stock.py
```

La opción `-i` en el comando `python3` le dice a Python que inicie una shell interactiva después de ejecutar el archivo `stock.py`. De esta manera, podemos interactuar directamente con la clase `Stock` que acabamos de definir.

En la shell de Python, creemos un objeto de tipo stock y probemos a acceder a sus atributos. Aquí está cómo puedes hacerlo:

```python
s = Stock('GOOG', 100, 490.10)
s.name      # Should return 'GOOG'
s.shares    # Should return 100
```

Cuando accedes a los atributos `name` y `shares` del objeto `s`, Python está usando en realidad el método `__get__` del descriptor detrás de escena. Los decoradores `property` en nuestra clase se implementan utilizando descriptores, lo que significa que manejan el acceso y la asignación de atributos de manera controlada.

Echemos un vistazo más de cerca al diccionario de la clase para ver los objetos descriptor. El diccionario de la clase contiene todos los atributos y métodos definidos en la clase. Puedes ver las claves del diccionario de la clase utilizando el siguiente código:

```python
Stock.__dict__.keys()
```

Deberías ver una salida similar a esta:

```
dict_keys(['__module__', '__slots__', '__init__', 'name', '_name', 'shares', '_shares', 'price', '_price', 'cost', 'sell', '__repr__', '__doc__'])
```

Las claves `name`, `shares` y `price` representan los objetos descriptor creados por los decoradores `property`.

Ahora, examinemos cómo funcionan los descriptores llamando manualmente a sus métodos. Usaremos el descriptor `shares` como ejemplo. Aquí está cómo puedes hacerlo:

```python
# Get the descriptor object for 'shares'
q = Stock.__dict__['shares']

# Use the __get__ method to retrieve the value
q.__get__(s, Stock)  # Should return 100

# Use the __set__ method to set a new value
q.__set__(s, 75)
s.shares  # Should now be 75

# Try to set an invalid value
try:
    q.__set__(s, '75')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

Cuando accedes a un atributo como `s.shares`, Python llama al método `__get__` del descriptor para recuperar el valor. Cuando asignas un valor como `s.shares = 75`, Python llama al método `__set__` del descriptor. El descriptor puede entonces validar los datos y lanzar errores si el valor de entrada no es válido.

Una vez que hayas terminado de experimentar con la clase `Stock` y los descriptores, puedes salir de la shell de Python ejecutando el siguiente comando:

```python
exit()
```
