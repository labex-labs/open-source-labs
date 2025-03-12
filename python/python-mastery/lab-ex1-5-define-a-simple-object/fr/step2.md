# Création de la classe Stock

En Python, une classe est un modèle pour créer des objets. Elle vous permet de regrouper des données et des fonctionnalités ensemble. Maintenant, créons notre classe `Stock` pour représenter des informations sur les actions (stocks). Une action a certaines caractéristiques, telles que son nom, le nombre de parts et le prix par part. Nous allons définir des attributs pour ces aspects au sein de notre classe.

1. Tout d'abord, vous devez être dans le bon répertoire dans le WebIDE. Si vous n'êtes pas déjà dans le répertoire `/home/labex/project`, naviguez jusqu'à celui-ci. C'est là que nous allons travailler sur le code de notre classe `Stock`.

2. Une fois que vous êtes dans le bon répertoire, créez un nouveau fichier dans l'éditeur. Nommez ce fichier `stock.py`. Ce fichier contiendra le code de notre classe `Stock`.

3. Maintenant, ajoutons le code pour définir la classe `Stock`. Copiez et collez le code suivant dans le fichier `stock.py` :

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
```

Dans ce code :

- La déclaration `class Stock:` crée une nouvelle classe nommée `Stock`. C'est comme un modèle pour créer des objets d'actions.
- La méthode `__init__` est une méthode spéciale dans les classes Python. Elle est appelée un constructeur. Lorsque vous créez un nouvel objet de la classe `Stock`, la méthode `__init__` s'exécutera automatiquement. Elle prend trois paramètres : `name`, `shares` et `price`. Ces paramètres représentent les informations sur l'action.
- À l'intérieur de la méthode `__init__`, nous utilisons `self` pour faire référence à l'instance de la classe. Nous stockons les valeurs des paramètres en tant qu'attributs d'instance. Par exemple, `self.name = name` stocke le paramètre `name` en tant qu'attribut de l'objet.
- La méthode `cost()` est une méthode personnalisée que nous avons définie. Elle calcule le coût total de l'action en multipliant le nombre de parts (`self.shares`) par le prix par part (`self.price`).

4. Après avoir ajouté le code, enregistrez le fichier. Vous pouvez le faire en appuyant sur `Ctrl+S` ou en cliquant sur l'icône Enregistrer. Enregistrer le fichier garantit que vos modifications sont conservées.

Examinons à nouveau le code pour nous assurer de le comprendre :

- Nous avons défini une classe nommée `Stock`. Cette classe sera utilisée pour créer des objets d'actions.
- La méthode `__init__` prend trois paramètres : `name`, `shares` et `price`. Elle initialise les attributs de l'objet avec ces valeurs.
- À l'intérieur de `__init__`, nous stockons ces paramètres en tant qu'attributs d'instance en utilisant `self`. Cela permet à chaque objet d'avoir son propre ensemble de valeurs pour ces attributs.
- Nous avons ajouté une méthode `cost()` qui calcule le coût total en multipliant le nombre de parts par le prix. C'est une fonctionnalité utile pour nos objets d'actions.

Lorsque nous créons un objet `Stock`, la méthode `__init__` s'exécutera automatiquement, configurant l'état initial de notre objet avec les valeurs que nous fournissons. De cette manière, nous pouvons facilement créer plusieurs objets d'actions avec différents noms, nombres de parts et prix.
