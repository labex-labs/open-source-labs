# Implementación de la Validación de Propiedades

Las propiedades (properties) también le permiten controlar cómo se recuperan, establecen y eliminan los valores de los atributos. Esto es útil para añadir validación a sus atributos, asegurando que los valores cumplen criterios específicos.

En nuestra clase `Stock`, queremos asegurar que `shares` sea un entero no negativo y que `price` sea un flotante no negativo. Utilizaremos decoradores de propiedad junto con _getters_ y _setters_ para lograr esto.

**Instrucciones:**

1.  Abra el archivo `stock.py` en el editor.

2.  Añada atributos privados `_shares` y `_price` a la clase `Stock` y modifique el constructor para utilizarlos:

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares  # Using private attribute
        self._price = price    # Using private attribute
    ```

3.  Defina propiedades para `shares` y `price` con validación:

    ```python
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected integer")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Expected float")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value
    ```

4.  Actualice el constructor para utilizar los _setters_ de propiedad para la validación:

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares  # Using property setter
        self.price = price    # Using property setter
    ```

5.  Guarde el archivo `stock.py`.

6.  Cree un script de prueba llamado `test_validation.py`:

    ```bash
    touch /home/labex/project/test_validation.py
    ```

7.  Añada el siguiente código al archivo `test_validation.py`:

    ```python
    from stock import Stock

    # Create a valid stock instance
    s = Stock('GOOG', 100, 490.10)
    print(f"Initial: Name={s.name}, Shares={s.shares}, Price={s.price}, Cost={s.cost}")

    # Test valid updates
    try:
        s.shares = 50  # Valid update
        print(f"After setting shares=50: Shares={s.shares}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting shares=50: {e}")

    try:
        s.price = 123.45  # Valid update
        print(f"After setting price=123.45: Price={s.price}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting price=123.45: {e}")

    # Test invalid updates
    try:
        s.shares = "50"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares='50': {e}")

    try:
        s.shares = -10  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares=-10: {e}")

    try:
        s.price = "123.45"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price='123.45': {e}")

    try:
        s.price = -10.0  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price=-10.0: {e}")
    ```

8.  Ejecute el script de prueba:

    ```bash
    python /home/labex/project/test_validation.py
    ```

    Debería ver una salida que muestre actualizaciones válidas exitosas y mensajes de error apropiados para actualizaciones no válidas.

    ```plaintext
    Initial: Name=GOOG, Shares=100, Price=490.1, Cost=49010.0
    After setting shares=50: Shares=50, Cost=24505.0
    After setting price=123.45: Price=123.45, Cost=6172.5
    Error setting shares='50': Expected integer
    Error setting shares=-10: shares must be >= 0
    Error setting price='123.45': Expected float
    Error setting price=-10.0: price must be >= 0
    ```
