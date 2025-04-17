# Implémentation de la validation des propriétés

Les propriétés vous permettent également de contrôler la manière dont les valeurs des attributs sont récupérées, définies et supprimées. Ceci est utile pour ajouter une validation à vos attributs, en vous assurant que les valeurs répondent à des critères spécifiques.

Dans notre classe `Stock`, nous voulons nous assurer que `shares` est un entier non négatif et que `price` est un flottant non négatif. Nous utiliserons des décorateurs de propriété (property decorators) avec des getters et des setters pour y parvenir.

**Instructions :**

1.  Ouvrez le fichier `stock.py` dans l'éditeur.

2.  Ajoutez les attributs privés `_shares` et `_price` à la classe `Stock` et modifiez le constructeur pour les utiliser :

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares  # Using private attribute
        self._price = price    # Using private attribute
    ```

3.  Définissez des propriétés pour `shares` et `price` avec validation :

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

4.  Mettez à jour le constructeur pour utiliser les setters de propriété pour la validation :

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares  # Using property setter
        self.price = price    # Using property setter
    ```

5.  Enregistrez le fichier `stock.py`.

6.  Créez un script de test nommé `test_validation.py` :

    ```bash
    touch /home/labex/project/test_validation.py
    ```

7.  Ajoutez le code suivant au fichier `test_validation.py` :

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

8.  Exécutez le script de test :

    ```bash
    python /home/labex/project/test_validation.py
    ```

    Vous devriez voir une sortie montrant les mises à jour valides réussies et les messages d'erreur appropriés pour les mises à jour non valides.

    ```plaintext
    Initial: Name=GOOG, Shares=100, Price=490.1, Cost=49010.0
    After setting shares=50: Shares=50, Cost=24505.0
    After setting price=123.45: Price=123.45, Cost=6172.5
    Error setting shares='50': Expected integer
    Error setting shares=-10: shares must be >= 0
    Error setting price='123.45': Expected float
    Error setting price=-10.0: price must be >= 0
    ```
