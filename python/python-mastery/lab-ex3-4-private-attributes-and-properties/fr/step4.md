# Utilisation de `__slots__` pour l'optimisation de la mémoire

En Python, l'attribut `__slots__` est un outil spécial qui peut vous aider à gérer vos classes plus efficacement. Il restreint les attributs qu'une classe peut avoir. Normalement, Python stocke les attributs d'instance dans un dictionnaire appelé `__dict__`, ce qui permet l'ajout dynamique de nouveaux attributs. Cependant, lorsque vous définissez `__slots__`, Python crée une structure statique pour les instances. Cela a deux effets principaux : il empêche l'ajout de nouveaux attributs aux instances, et il réduit l'utilisation de la mémoire car il n'a pas besoin de maintenir le `__dict__`.

Dans notre classe `Stock`, nous allons utiliser `__slots__` pour deux raisons importantes :

1. Pour restreindre la création d'attributs aux seuls attributs que nous avons définis. Cela signifie que les utilisateurs de la classe ne peuvent pas ajouter accidentellement ou intentionnellement de nouveaux attributs que nous n'avons pas prévus.
2. Pour améliorer l'efficacité mémoire, en particulier lors de la création de nombreuses instances. Si vous avez un grand nombre d'objets de la classe `Stock`, l'utilisation de `__slots__` peut économiser une quantité significative de mémoire.

## Instructions :

1. Tout d'abord, vous devez ouvrir le fichier `stock.py` dans l'éditeur. C'est là que nous allons apporter des modifications à la classe `Stock`. Utilisez la commande suivante dans le terminal :

   ```bash
   code /home/labex/project/stock.py
   ```

2. À l'intérieur du fichier `stock.py`, nous allons ajouter une variable de classe `__slots__`. Cette variable doit lister tous les noms d'attributs privés utilisés par la classe. Voici comment faire :

   ```python
   class Stock:
       # Class variable for type conversions
       _types = (str, int, float)

       # Define slots to restrict attribute creation
       __slots__ = ('name', '_shares', '_price')

       # Rest of the class...
   ```

   En définissant `__slots__` de cette manière, nous indiquons à Python que les instances de la classe `Stock` ne peuvent avoir que les attributs `name`, `_shares` et `_price`.

3. Après avoir apporté ces modifications, enregistrez le fichier. Cela garantit que vos modifications sont conservées.

4. Maintenant, nous devons créer un script de test pour vérifier que `__slots__` fonctionne comme prévu. Ouvrez un nouveau fichier nommé `test_slots.py` en utilisant la commande suivante :

   ```bash
   code /home/labex/project/test_slots.py
   ```

5. Ajoutez le code suivant au fichier `test_slots.py`. Ce code créera une instance de la classe `Stock`, accédera à ses attributs existants, puis tentera d'ajouter un nouvel attribut.

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

   Le bloc `try` tente d'ajouter un nouvel attribut `extra` à l'instance `s` de la classe `Stock`. Si `__slots__` fonctionne correctement, cela devrait lever une `AttributeError` car `extra` n'est pas répertorié dans `__slots__`.

6. Enfin, exécutez le script de test en utilisant la commande suivante :
   ```bash
   python /home/labex/project/test_slots.py
   ```

Vous devriez voir une sortie montrant que vous pouvez accéder aux attributs définis, mais que la tentative d'ajouter un nouvel attribut lève une `AttributeError`. Cela confirme que `__slots__` fonctionne comme prévu.

### Comprendre `__slots__`

Lorsque vous utilisez `__slots__`, il est important de garder les points suivants à l'esprit :

1. Vous devez lister tous les attributs qui seront stockés sur l'instance. Si vous oubliez de lister un attribut, vous ne pourrez pas l'affecter à l'instance.
2. Seuls les attributs répertoriés dans `__slots__` peuvent être affectés aux instances. Cela contribue à imposer une structure stricte à vos objets.
3. Les instances n'auront plus d'attribut `__dict__`. Étant donné que `__slots__` crée une structure statique, il n'y a pas besoin du dictionnaire dynamique.
4. Les sous-classes n'hériteront pas des `__slots__` de leur classe mère à moins qu'elles ne définissent leurs propres `__slots__`. Cela signifie que les sous-classes ont la flexibilité de définir leurs propres restrictions d'attributs.

Les principaux avantages de l'utilisation de `__slots__` sont :

1. **Efficacité mémoire** : Les instances utilisent moins de mémoire car il n'y a pas de `__dict__` pour stocker les attributs.
2. **Vitesse** : L'accès aux attributs est légèrement plus rapide car Python n'a pas besoin de rechercher l'attribut dans un dictionnaire.
3. **Prévention de la création accidentelle d'attributs** : Aide à détecter les fautes de frappe et les erreurs de programmation en empêchant l'ajout d'attributs inattendus.
