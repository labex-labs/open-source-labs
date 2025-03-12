# Mise en œuvre d'attributs privés

En Python, lorsque nous concevons une classe, certains attributs sont destinés à être utilisés uniquement à l'intérieur de la classe elle - même. Ces attributs font partie de l'implémentation interne de la classe. Pour indiquer cela aux autres développeurs, nous suivons une convention de nommage. Nous préfixons ces attributs internes d'un trait de soulignement (`_`). C'est comme un signe indiquant que ces attributs ne font pas partie de l'API publique. L'API publique est l'ensemble des méthodes et des attributs avec lesquels les autres parties du code sont censées interagir. Ainsi, les attributs avec un trait de soulignement ne devraient pas être accédés directement depuis l'extérieur de la classe.

Regardons la classe `Stock` actuelle dans le fichier `stock.py`. Cette classe est utilisée pour représenter des actions (stocks), et elle a une variable de classe nommée `types`.

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

La variable de classe `types` est utilisée à l'intérieur de la classe pour convertir les données de ligne. Par exemple, lorsque nous obtenons des données dans une ligne, nous utilisons ces types pour convertir les données au bon format. Étant donné que ce n'est qu'un détail d'implémentation et que ce n'est pas quelque chose avec lequel les autres parties du code devraient interagir directement, nous devrions le marquer comme privé.

## Instructions :

1. Tout d'abord, nous devons ouvrir le fichier `stock.py` dans l'éditeur. Nous pouvons le faire en utilisant la commande suivante dans le terminal. Cette commande ouvrira le fichier dans l'éditeur de code.

   ```bash
   code /home/labex/project/stock.py
   ```

2. Maintenant, nous allons modifier la variable de classe `types`. Nous ajoutons un trait de soulignement au début, la rendant `_types`. Ce changement indique que cette variable est privée et ne devrait pas être accédée directement depuis l'extérieur de la classe.

   ```python
   class Stock:
       # Class variable for type conversions
       _types = (str, int, float)

       # Rest of the class...
   ```

3. Après avoir renommé la variable, nous devons mettre à jour la méthode `from_row`. Cette méthode utilise la variable `types` pour convertir les données de ligne. Maintenant que nous l'avons renommée en `_types`, nous devons mettre à jour la méthode en conséquence.

   ```python
   @classmethod
   def from_row(cls, row):
       values = [func(val) for func, val in zip(cls._types, row)]
       return cls(*values)
   ```

4. Une fois que nous avons apporté ces modifications, nous devons enregistrer le fichier. Enregistrer le fichier garantit que nos modifications sont stockées et peuvent être utilisées plus tard.

5. Pour tester nos modifications, nous allons créer un script Python appelé `test_stock.py`. Nous pouvons ouvrir le fichier dans l'éditeur en utilisant la commande suivante.

   ```bash
   code /home/labex/project/test_stock.py
   ```

6. Maintenant, nous ajoutons le code suivant au fichier `test_stock.py`. Ce code crée des instances de la classe `Stock`, à la fois directement et en utilisant la méthode `from_row`. Il affiche ensuite des informations sur ces instances, telles que le nom, le nombre d'actions, le prix et le coût.

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

7. Enfin, nous exécutons le script de test en utilisant la commande suivante dans le terminal. Cela exécutera le code dans le fichier `test_stock.py` et nous montrera la sortie.

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
