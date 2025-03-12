# Création d'une classe simple pour les actions

Dans cette étape, nous allons créer une classe simple pour représenter une action. Comprendre comment créer des classes est fondamental en Python, car cela nous permet de modéliser des objets du monde réel et leurs comportements. Cette classe simple pour les actions sera notre point de départ pour explorer le fonctionnement interne des objets Python.

Pour commencer, nous devons ouvrir un shell interactif Python. Le shell interactif Python est un excellent endroit pour expérimenter avec le code Python. Vous pouvez taper et exécuter des commandes Python une par une. Pour l'ouvrir, tapez la commande suivante dans le terminal :

```bash
python3
```

Une fois que vous avez entré la commande, vous verrez l'invite Python (`>>>`). Cela indique que vous êtes maintenant dans le shell interactif Python et que vous pouvez commencer à écrire du code Python.

Maintenant, définissons une classe `SimpleStock`. Une classe en Python est comme un modèle pour créer des objets. Elle définit les attributs (données) et les méthodes (fonctions) que les objets de cette classe auront. Voici comment définir la classe `SimpleStock` avec les attributs et les méthodes nécessaires :

```python
>>> class SimpleStock:
...     def __init__(self, name, shares, price):
...         self.name = name
...         self.shares = shares
...         self.price = price
...     def cost(self):
...         return self.shares * self.price
...
```

Dans le code ci - dessus, la méthode `__init__` est une méthode spéciale dans les classes Python. C'est ce qu'on appelle un constructeur, et il est utilisé pour initialiser les attributs de l'objet lorsqu'un objet est créé. Le paramètre `self` fait référence à l'instance de la classe qui est en cours de création. La méthode `cost` calcule le coût total des actions en multipliant le nombre d'actions par le prix unitaire.

Après avoir défini la classe, nous pouvons créer des instances de la classe `SimpleStock`. Une instance est un objet réel créé à partir du modèle de la classe. Créons deux instances pour représenter différentes actions :

```python
>>> goog = SimpleStock('GOOG', 100, 490.10)
>>> ibm = SimpleStock('IBM', 50, 91.23)
```

Ces instances représentent 100 actions de Google au prix de 490,10 $ par action et 50 actions d'IBM au prix de 91,23 $ par action. Chaque instance a son propre ensemble de valeurs d'attributs.

Vérifions que nos instances fonctionnent correctement. Nous pouvons le faire en vérifiant leurs attributs et en calculant leur coût. Cela nous aidera à confirmer que la classe et ses méthodes fonctionnent comme prévu.

```python
>>> goog.name
'GOOG'
>>> goog.shares
100
>>> goog.price
490.1
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
```

La méthode `cost()` multiplie le nombre d'actions par le prix unitaire pour calculer le coût total de détention de ces actions. En exécutant ces commandes, nous pouvons voir que les instances ont les bonnes valeurs d'attributs et que la méthode `cost` calcule le coût avec précision.
