# Utilisation de `__slots__` pour l'optimisation de la mémoire

L'attribut `__slots__` restreint les attributs qu'une classe peut avoir. Il empêche l'ajout de nouveaux attributs aux instances et réduit l'utilisation de la mémoire.

Dans notre classe `Stock`, nous utiliserons `__slots__` pour :

1.  Restreindre la création d'attributs aux seuls attributs que nous avons définis.
2.  Améliorer l'efficacité de la mémoire, en particulier lors de la création de nombreuses instances.

**Instructions :**

1.  Ouvrez le fichier `stock.py` dans l'éditeur.
2.  Ajoutez une variable de classe `__slots__`, en listant tous les noms d'attributs privés utilisés par la classe :

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Define slots to restrict attribute creation
        __slots__ = ('name', '_shares', '_price')

        # Rest of the class...
    ```

3.  Enregistrez le fichier.

4.  Créez un script de test nommé `test_slots.py` :

    ```bash
    touch /home/labex/project/test_slots.py
    ```

5.  Ajoutez le code suivant au fichier `test_slots.py` :

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access existing attributes
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")

    # Try to add a new attribute
    try:
        s.extra = "This will fail"
        print(f"Extra: {s.extra}")
    except AttributeError as e:
        print(f"Error: {e}")
    ```

6.  Exécutez le script de test :

    ```bash
    python /home/labex/project/test_slots.py
    ```

    Vous devriez voir une sortie montrant que vous pouvez accéder aux attributs définis, mais que tenter d'ajouter un nouvel attribut lève une `AttributeError`.

    ```plaintext
    Name: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    Error: 'Stock' object has no attribute 'extra'
    ```
