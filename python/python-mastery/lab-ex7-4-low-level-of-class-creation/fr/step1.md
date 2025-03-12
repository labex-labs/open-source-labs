# Création manuelle de classe

En programmation Python, les classes sont un concept fondamental qui vous permet de regrouper des données et des fonctions. Habituellement, nous définissons des classes en utilisant la syntaxe standard de Python. Par exemple, voici une simple classe `Stock`. Cette classe représente une action avec des attributs tels que `name`, `shares` et `price`, et elle a des méthodes pour calculer le coût et vendre des actions.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Mais avez-vous déjà vous demandé comment Python crée réellement une classe en coulisse ? Et si nous voulions créer cette classe sans utiliser la syntaxe standard des classes ? Dans cette section, nous allons explorer comment les classes Python sont construites au niveau inférieur.

## Lancer le shell interactif Python

Pour commencer à expérimenter la création manuelle de classes, nous devons ouvrir un shell interactif Python. Ce shell nous permet d'exécuter le code Python ligne par ligne, ce qui est idéal pour apprendre et tester.

Ouvrez un terminal dans WebIDE et lancez le shell interactif Python en tapant les commandes suivantes. La première commande `cd ~/project` change le répertoire courant pour le répertoire du projet, et la deuxième commande `python3` lance le shell interactif Python 3.

```bash
cd ~/project
python3
```

## Définition des méthodes comme des fonctions ordinaires

Avant de créer une classe manuellement, nous devons définir les méthodes qui feront partie de la classe. En Python, les méthodes ne sont que des fonctions associées à une classe. Donc, définissons les méthodes que nous voulons dans notre classe comme des fonctions Python ordinaires.

```python
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

def sell(self, nshares):
    self.shares -= nshares
```

Ici, la fonction `__init__` est une méthode spéciale dans les classes Python. C'est ce qu'on appelle un constructeur, et il est utilisé pour initialiser les attributs de l'objet lorsqu'une instance de la classe est créée. La méthode `cost` calcule le coût total des actions, et la méthode `sell` réduit le nombre d'actions.

## Création d'un dictionnaire de méthodes

Maintenant que nous avons défini nos méthodes comme des fonctions ordinaires, nous devons les organiser d'une manière que Python puisse comprendre lors de la création de la classe. Nous le faisons en créant un dictionnaire qui contiendra toutes les méthodes de notre classe.

```python
methods = {
    '__init__': __init__,
    'cost': cost,
    'sell': sell
}
```

Dans ce dictionnaire, les clés sont les noms des méthodes telles qu'elles seront utilisées dans la classe, et les valeurs sont les objets de fonction que nous avons définis précédemment.

## Utilisation du constructeur type() pour créer une classe

En Python, la fonction `type()` est une fonction intégrée qui peut être utilisée pour créer des classes au niveau inférieur. La fonction `type()` prend trois arguments :

1. Le nom de la classe : C'est une chaîne de caractères qui représente le nom de la classe que nous voulons créer.
2. Un tuple de classes de base : En Python, les classes peuvent hériter d'autres classes. Ici, nous utilisons `(object,)` ce qui signifie que notre classe hérite de la classe de base `object`, qui est la classe de base de toutes les classes en Python.
3. Un dictionnaire contenant les méthodes et les attributs : C'est le dictionnaire que nous avons créé précédemment qui contient toutes les méthodes de notre classe.

```python
Stock = type('Stock', (object,), methods)
```

Cette ligne de code crée une nouvelle classe nommée `Stock` en utilisant la fonction `type()`. La classe hérite de la classe `object` et a les méthodes définies dans le dictionnaire `methods`.

## Test de notre classe créée manuellement

Maintenant que nous avons créé notre classe manuellement, testons-la pour nous assurer qu'elle fonctionne comme prévu. Nous allons créer une instance de notre nouvelle classe et appeler ses méthodes.

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
s.sell(25)
print(s.shares)
```

Dans la première ligne, nous créons une instance de la classe `Stock` avec le nom `GOOG`, 100 actions et un prix de 490,10. Ensuite, nous affichons le nom de l'action, calculons et affichons le coût, vendons 25 actions et, enfin, affichons le nombre restant d'actions.

Vous devriez voir la sortie suivante :

```
GOOG
49010.0
75
```

Cette sortie montre que notre classe créée manuellement fonctionne tout comme une classe créée en utilisant la syntaxe standard de Python. Cela démontre qu'une classe est fondamentalement juste un nom, un tuple de classes de base et un dictionnaire de méthodes et d'attributs. La fonction `type()` construit simplement un objet de classe à partir de ces composants.

Quittez le shell Python lorsque vous avez terminé :

```python
exit()
```
