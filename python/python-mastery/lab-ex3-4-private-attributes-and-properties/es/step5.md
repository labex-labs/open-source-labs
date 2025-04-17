# Conciliando la Validación de Tipos con Variables de Clase

Actualmente, nuestra clase `Stock` utiliza tanto la variable de clase `_types` como los _setters_ de propiedad para el manejo de tipos. Para mejorar la consistencia y la mantenibilidad, reconciliaremos estos mecanismos para que utilicen la misma información de tipo.

**Instrucciones:**

1.  Abra el archivo `stock.py` en el editor.

2.  Modifique los _setters_ de propiedad para utilizar los tipos definidos en la variable de clase `_types`:

    ```python
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected {self._types[1].__name__}")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected {self._types[2].__name__}")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value
    ```

3.  Guarde el archivo `stock.py`.

4.  Cree un script de prueba llamado `test_subclass.py`:

    ```bash
    touch /home/labex/project/test_subclass.py
    ```

5.  Añada el siguiente código al archivo `test_subclass.py`:

    ```python
    from stock import Stock
    from decimal import Decimal

    # Create a subclass with different types
    class DStock(Stock):
        _types = (str, int, Decimal)

    # Test the base class
    s = Stock('GOOG', 100, 490.10)
    print(f"Stock: {s.name}, Shares: {s.shares}, Price: {s.price}, Cost: {s.cost}")

    # Test valid update with float
    try:
        s.price = 500.25
        print(f"Updated Stock price: {s.price}, Cost: {s.cost}")
    except Exception as e:
        print(f"Error updating Stock price: {e}")

    # Test the subclass with Decimal
    ds = DStock('AAPL', 50, Decimal('142.50'))
    print(f"DStock: {ds.name}, Shares: {ds.shares}, Price: {ds.price}, Cost: {ds.cost}")

    # Test invalid update with float (should require Decimal)
    try:
        ds.price = 150.75
        print(f"Updated DStock price: {ds.price}")
    except Exception as e:
        print(f"Error updating DStock price: {e}")

    # Test valid update with Decimal
    try:
        ds.price = Decimal('155.25')
        print(f"Updated DStock price: {ds.price}, Cost: {ds.cost}")
    except Exception as e:
        print(f"Error updating DStock price: {e}")
    ```

6.  Ejecute el script de prueba:

    ```bash
    python /home/labex/project/test_subclass.py
    ```

    Debería ver que la clase base `Stock` acepta valores _float_ para el precio, mientras que la subclase `DStock` requiere valores `Decimal`.

    ```plaintext
    Stock: GOOG, Shares: 100, Price: 490.1, Cost: 49010.0
    Updated Stock price: 500.25, Cost: 50025.0
    DStock: AAPL, Shares: 50, Price: 142.50, Cost: 7125.00
    Error updating DStock price: Expected Decimal
    Updated DStock price: 155.25, Cost: 7762.50
    ```
