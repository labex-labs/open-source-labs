# Implémentation d'attributs privés

En Python, nous utilisons une convention de nommage pour indiquer qu'un attribut est destiné à un usage interne au sein d'une classe. Nous préfixons ces attributs avec un underscore (`_`). Cela signale aux autres développeurs que ces attributs ne font pas partie de l'API publique et ne doivent pas être accessibles directement depuis l'extérieur de la classe.

Examinons la classe `Stock` actuelle dans le fichier `stock.py`. Elle possède une variable de classe nommée `types`.

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

La variable de classe `types` est utilisée en interne pour convertir les données des lignes. Pour indiquer qu'il s'agit d'un détail d'implémentation, nous allons la marquer comme privée.

**Instructions :**

1.  Ouvrez le fichier `stock.py` dans l'éditeur.

2.  Modifiez la variable de classe `types` en ajoutant un underscore au début, en la remplaçant par `_types`.

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Rest of the class...
    ```

3.  Mettez à jour la méthode `from_row` pour utiliser la variable renommée `_types`.

    ```python
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    ```

4.  Enregistrez le fichier `stock.py`.

5.  Créez un script Python nommé `test_stock.py` pour tester vos modifications. Vous pouvez créer le fichier dans l'éditeur en utilisant la commande suivante :

    ```bash
    touch /home/labex/project/test_stock.py
    ```

6.  Ajoutez le code suivant au fichier `test_stock.py`. Ce code crée des instances de la classe `Stock` et affiche des informations à leur sujet.

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)
    print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
    print(f"Cost: {s.cost()}")

    # Create from row
    row = ['AAPL', '50', '142.5']
    apple = Stock.from_row(row)
    print(f"Name: {apple.name}, Shares: {apple.shares}, Price: {apple.price}")
    print(f"Cost: {apple.cost()}")
    ```

7.  Exécutez le script de test en utilisant la commande suivante dans le terminal :

    ```bash
    python /home/labex/project/test_stock.py
    ```

    Vous devriez voir une sortie similaire à :

    ```
    Name: GOOG, Shares: 100, Price: 490.1
    Cost: 49010.0
    Name: AAPL, Shares: 50, Price: 142.5
    Cost: 7125.0
    ```
