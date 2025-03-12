# Création d'objets en lecture seule avec des proxies

Dans cette étape, nous allons explorer les classes proxy, un modèle très utile en Python. Les classes proxy vous permettent de prendre un objet existant et de modifier son comportement sans altérer son code d'origine. C'est comme mettre une enveloppe spéciale autour d'un objet pour ajouter de nouvelles fonctionnalités ou des restrictions.

## Qu'est-ce qu'un proxy ?

Un proxy est un objet qui se place entre vous et un autre objet. Il a le même ensemble de fonctions et de propriétés que l'objet d'origine, mais il peut faire des choses supplémentaires. Par exemple, il peut contrôler qui peut accéder à l'objet, conserver un enregistrement des actions (journalisation) ou ajouter d'autres fonctionnalités utiles.

Créons un proxy en lecture seule. Ce type de proxy vous empêchera de modifier les attributs d'un objet.

### Étape 1 : Créer la classe de proxy en lecture seule

Tout d'abord, nous devons créer un fichier Python qui définit notre proxy en lecture seule.

1. Accédez au répertoire `/home/labex/project`.
2. Créez un nouveau fichier nommé `readonly_proxy.py` dans ce répertoire.
3. Ouvrez le fichier `readonly_proxy.py` et ajoutez le code suivant :

```python
class ReadonlyProxy:
    def __init__(self, obj):
        # Store the wrapped object directly in __dict__ to avoid triggering __setattr__
        self.__dict__['_obj'] = obj

    def __getattr__(self, name):
        # Forward attribute access to the wrapped object
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        # Block all attribute assignments
        raise AttributeError("Cannot modify a read-only object")
```

Dans ce code, la classe `ReadonlyProxy` est définie. La méthode `__init__` stocke l'objet que nous voulons envelopper. Nous utilisons `self.__dict__` pour le stocker directement afin d'éviter d'appeler la méthode `__setattr__`. La méthode `__getattr__` est utilisée lorsque nous essayons d'accéder à un attribut du proxy. Elle transmet simplement la demande à l'objet enveloppé. La méthode `__setattr__` est appelée lorsque nous essayons de modifier un attribut. Elle lève une erreur pour empêcher toute modification.

### Étape 2 : Créer un fichier de test

Maintenant, nous allons créer un fichier de test pour voir comment fonctionne notre proxy en lecture seule.

1. Créez un nouveau fichier nommé `test_readonly.py` dans le même répertoire `/home/labex/project`.
2. Ajoutez le code suivant au fichier `test_readonly.py` :

```python
from stock import Stock
from readonly_proxy import ReadonlyProxy

# Create a normal Stock object
stock = Stock('AAPL', 100, 150.75)
print("Original stock object:")
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")
print(f"Cost: {stock.cost}")

# Modify the original stock object
stock.shares = 200
print(f"\nAfter modification - Shares: {stock.shares}")
print(f"After modification - Cost: {stock.cost}")

# Create a read-only proxy around the stock
readonly_stock = ReadonlyProxy(stock)
print("\nRead-only proxy object:")
print(f"Name: {readonly_stock.name}")
print(f"Shares: {readonly_stock.shares}")
print(f"Price: {readonly_stock.price}")
print(f"Cost: {readonly_stock.cost}")

# Try to modify the read-only proxy
try:
    print("\nAttempting to modify the read-only proxy...")
    readonly_stock.shares = 300
except AttributeError as e:
    print(f"Error: {e}")

# Show that the original object is unchanged
print(f"\nOriginal stock shares are still: {stock.shares}")
```

Dans ce code de test, nous créons d'abord un objet `Stock` normal et affichons ses informations. Ensuite, nous modifions l'un de ses attributs et affichons les informations mises à jour. Ensuite, nous créons un proxy en lecture seule pour l'objet `Stock` et affichons ses informations. Enfin, nous essayons de modifier le proxy en lecture seule et nous nous attendons à recevoir une erreur.

### Étape 3 : Exécuter le script de test

Après avoir créé la classe de proxy et le fichier de test, nous devons exécuter le script de test pour voir les résultats.

1. Ouvrez un terminal et accédez au répertoire `/home/labex/project` en utilisant la commande suivante :

```bash
cd /home/labex/project
```

2. Exécutez le script de test en utilisant la commande suivante :

```bash
python3 test_readonly.py
```

Vous devriez voir une sortie similaire à :

```
Original stock object:
Name: AAPL
Shares: 100
Price: 150.75
Cost: 15075.0

After modification - Shares: 200
After modification - Cost: 30150.0

Read-only proxy object:
Name: AAPL
Shares: 200
Price: 150.75
Cost: 30150.0

Attempting to modify the read-only proxy...
Error: Cannot modify a read-only object

Original stock shares are still: 200
```

## Comment le proxy fonctionne

La classe `ReadonlyProxy` utilise deux méthodes spéciales pour obtenir sa fonctionnalité en lecture seule :

1. `__getattr__(self, name)` : Cette méthode est appelée lorsque Python ne peut pas trouver un attribut de la manière normale. Dans notre classe `ReadonlyProxy`, nous utilisons la fonction `getattr()` pour transférer la demande d'accès à l'attribut à l'objet enveloppé. Donc, lorsque vous essayez d'accéder à un attribut du proxy, il obtiendra en fait l'attribut de l'objet enveloppé.

2. `__setattr__(self, name, value)` : Cette méthode est appelée lorsque vous essayez d'assigner une valeur à un attribut. Dans notre implémentation, nous levons une `AttributeError` pour empêcher toute modification des attributs du proxy.

3. Dans la méthode `__init__`, nous modifions directement `self.__dict__` pour stocker l'objet enveloppé. Cela est important car si nous utilisions la manière normale d'assigner l'objet, cela appellerait la méthode `__setattr__`, qui lèverait une erreur.

Ce modèle de proxy nous permet d'ajouter une couche en lecture seule autour de n'importe quel objet existant sans modifier sa classe d'origine. L'objet proxy se comporte comme l'objet enveloppé, mais ne vous laissera pas effectuer de modifications.
