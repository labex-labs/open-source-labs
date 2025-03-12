# Explorer l'héritage des métaclasses

Les métaclasses ont une caractéristique fascinante : elles sont « collantes ». Cela signifie qu'une fois qu'une classe utilise une métaclasse, toutes ses sous - classes dans la hiérarchie d'héritage utiliseront également la même métaclasse. En d'autres termes, la propriété de la métaclasse se propage à travers la chaîne d'héritage.

Voyons cela en action :

1. Tout d'abord, ouvrez le fichier `mymeta.py`. À la fin de ce fichier, nous allons ajouter une nouvelle classe. Cette classe, nommée `MyStock`, héritera de la classe `Stock`. La méthode `__init__` est utilisée pour initialiser les attributs de l'objet, et nous appelons la méthode `__init__` de la classe parente en utilisant `super().__init__` pour initialiser les attributs communs. La méthode `info` est utilisée pour retourner une chaîne formatée avec des informations sur les actions. Ajoutez le code suivant :

```python
class MyStock(Stock):
    def __init__(self, name, shares, price, category):
        super().__init__(name, shares, price)
        self.category = category

    def info(self):
        return f"{self.name} ({self.category}): {self.shares} shares at ${self.price}"
```

2. Après avoir ajouté le code, enregistrez le fichier `mymeta.py`. Enregistrer le fichier garantit que les modifications que nous avons apportées sont enregistrées et peuvent être utilisées plus tard.

3. Maintenant, nous allons créer un nouveau fichier nommé `test_inheritance.py` pour tester le comportement d'héritage de la métaclasse. Dans ce fichier, nous allons importer la classe `MyStock` depuis le fichier `mymeta.py`. Ensuite, nous allons créer une instance de la classe `MyStock`, appeler ses méthodes et afficher les résultats pour voir comment la métaclasse fonctionne via l'héritage. Ajoutez le code suivant à `test_inheritance.py` :

```python
# test_inheritance.py
from mymeta import MyStock

# Create a MyStock instance
tech_stock = MyStock("MSFT", 50, 305.75, "Technology")

# Test the methods
print(tech_stock.info())
print(f"Total cost: ${tech_stock.cost()}")

# Sell some shares
tech_stock.sell(5)
print(f"After selling: {tech_stock.shares} shares remaining")
print(f"Updated cost: ${tech_stock.cost()}")
```

4. Enfin, exécutez le fichier `test_inheritance.py` pour voir la métaclasse en action via l'héritage. Ouvrez votre terminal, accédez au répertoire où se trouve le fichier `test_inheritance.py` et exécutez la commande suivante :

```bash
python3 test_inheritance.py
```

Vous devriez voir une sortie similaire à :

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Creating class : MyStock
Base classes   : (<class 'mymeta.Stock'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'info', '__doc__']
MSFT (Technology): 50 shares at $305.75
Total cost: $15287.5
After selling: 45 shares remaining
Updated cost: $13758.75
```

Remarquez que même si nous n'avons pas spécifié explicitement une métaclasse pour la classe `MyStock`, la métaclasse est toujours appliquée. Cela démontre clairement comment les métaclasses se propagent via l'héritage.

## Utilisations pratiques des métaclasses

Dans notre exemple, la métaclasse ne fait que afficher des informations sur les classes. Cependant, les métaclasses ont de nombreuses applications pratiques dans la programmation réelle :

1. **Validation** : Vous pouvez utiliser des métaclasses pour vérifier si une classe a les méthodes ou les attributs requis. Cela permet de s'assurer que les classes répondent à certains critères avant d'être utilisées.
2. **Enregistrement** : Les métaclasses peuvent enregistrer automatiquement les classes dans un registre. Cela est utile lorsque vous avez besoin de suivre toutes les classes d'un certain type.
3. **Respect des interfaces** : Elles peuvent être utilisées pour s'assurer que les classes implémentent les interfaces requises. Cela contribue à maintenir une structure cohérente dans votre code.
4. **Programmation orientée aspect** : Les métaclasses peuvent ajouter des comportements aux méthodes. Par exemple, vous pouvez ajouter une journalisation ou une surveillance des performances aux méthodes sans modifier directement le code de la méthode.
5. **Systèmes ORM** : Dans les systèmes de mappage objet - relationnel (ORM) comme Django ou SQLAlchemy, les métaclasses sont utilisées pour mapper les classes aux tables de base de données. Cela simplifie les opérations de base de données dans votre application.

Les métaclasses sont très puissantes, mais elles doivent être utilisées avec modération. Comme l'a dit un jour Tim Peters (connnu pour le Zen de Python) : « Les métaclasses sont une magie plus profonde que 99 % des utilisateurs n'auront jamais à se soucier. »
