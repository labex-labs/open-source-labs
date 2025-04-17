# Conciliation de la validation de type avec les variables de classe

Actuellement, notre classe `Stock` utilise à la fois la variable de classe `_types` et les setters de propriété (property setters) pour la gestion des types. Pour améliorer la cohérence et la maintenabilité, nous allons concilier ces mécanismes afin qu'ils utilisent les mêmes informations de type.

**Instructions :**

1.  Ouvrez le fichier `stock.py` dans l'éditeur.

2.  Modifiez les setters de propriété pour utiliser les types définis dans la variable de classe `_types` :

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

3.  Enregistrez le fichier `stock.py`.

4.  Créez un script de test nommé `test_subclass.py` :

    ```bash
    touch /home/labex/project/test_subclass.py
    ```

5.  Ajoutez le code suivant au fichier `test_subclass.py` :

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

6.  Exécutez le script de test :

    ```bash
    python /home/labex/project/test_subclass.py
    ```

    Vous devriez voir que la classe de base `Stock` accepte les valeurs float pour le prix, tandis que la sous-classe `DStock` exige des valeurs `Decimal`.

    ```plaintext
    Stock: GOOG, Shares: 100, Price: 490.1, Cost: 49010.0
    Updated Stock price: 500.25, Cost: 50025.0
    DStock: AAPL, Shares: 50, Price: 142.50, Cost: 7125.00
    Error updating DStock price: Expected Decimal
    Updated DStock price: 155.25, Cost: 7762.50
    ```
