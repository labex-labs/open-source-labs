# Conversion de méthodes en propriétés

Les propriétés (properties) en Python vous permettent d'accéder à des valeurs calculées comme des attributs. Cela élimine le besoin de parenthèses lors de l'appel d'une méthode, ce qui rend votre code plus propre et plus cohérent.

Actuellement, notre classe `Stock` possède une méthode `cost()` qui calcule le coût total des actions.

```python
def cost(self):
    return self.shares * self.price
```

Pour obtenir la valeur du coût, nous devons l'appeler avec des parenthèses :

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

Nous pouvons améliorer cela en convertissant la méthode `cost()` en une propriété, ce qui nous permet d'accéder à la valeur du coût sans parenthèses :

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

**Instructions :**

1.  Ouvrez le fichier `stock.py` dans l'éditeur.

2.  Remplacez la méthode `cost()` par une propriété en utilisant le décorateur `@property` :

    ```python
    @property
    def cost(self):
        return self.shares * self.price
    ```

3.  Enregistrez le fichier `stock.py`.

4.  Créez un nouveau fichier nommé `test_property.py` dans l'éditeur :

    ```bash
    touch /home/labex/project/test_property.py
    ```

5.  Ajoutez le code suivant au fichier `test_property.py` pour créer une instance `Stock` et accéder à la propriété `cost` :

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access cost as a property (no parentheses)
    print(f"Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")  # Using the property
    ```

6.  Exécutez le script de test :

    ```bash
    python /home/labex/project/test_property.py
    ```

    Vous devriez voir une sortie similaire à :

    ```
    Stock: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    ```
