# Comprendre le problème de l'initialisation de classe

Dans le monde de la programmation, les classes sont un concept fondamental qui vous permet de créer des types de données personnalisés. Dans les exercices précédents, vous avez peut-être créé une classe `Structure`. Cette classe est un outil utile pour définir facilement des structures de données. Une structure de données est une façon d'organiser et de stocker des données afin qu'elles puissent être accessibles et utilisées efficacement. La classe `Structure`, en tant que classe de base, s'occupe d'initialiser les attributs en fonction d'une liste prédéfinie de noms de champs. Les attributs sont des variables appartenant à un objet, et les noms de champs sont les noms que nous donnons à ces attributs.

Regardons de plus près l'implémentation actuelle de la classe `Structure`. Pour ce faire, nous devons ouvrir le fichier `structure.py` dans l'éditeur de code. Ce fichier contient le code de la classe `Structure`. Voici les commandes pour accéder au répertoire du projet et ouvrir le fichier :

```bash
cd ~/project
code structure.py
```

La classe `Structure` fournit un cadre de base pour définir des structures de données simples. Lorsque nous créons une sous-classe, comme la classe `Stock`, nous pouvons définir les champs spécifiques que nous voulons pour cette sous-classe. Une sous-classe hérite des propriétés et des méthodes de sa classe de base, dans ce cas, la classe `Structure`. Par exemple, dans la classe `Stock`, nous définissons les champs `name`, `shares` et `price` :

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')
```

Maintenant, ouvrons le fichier `stock.py` pour voir comment la classe `Stock` est implémentée dans le contexte du code global. Ce fichier contient probablement le code qui utilise la classe `Stock` et interagit avec elle. Utilisez la commande suivante pour ouvrir le fichier :

```bash
code stock.py
```

Bien que cette approche d'utilisation de la classe `Structure` et de ses sous-classes fonctionne, elle présente plusieurs limitations. Pour identifier ces problèmes, nous allons exécuter l'interpréteur Python et explorer le comportement de la classe `Stock`. La commande suivante importe la classe `Stock` et affiche son information d'aide :

```bash
python3 -c "from stock import Stock; help(Stock)"
```

Lorsque vous exécutez cette commande, vous remarquerez que la signature affichée dans la sortie d'aide n'est pas très utile. Au lieu d'afficher les noms de paramètres réels comme `name`, `shares` et `price`, elle n'affiche que `*args`. Ce manque de noms de paramètres clairs rend difficile pour les utilisateurs de comprendre comment créer correctement une instance de la classe `Stock`.

Essayons également de créer une instance de `Stock` en utilisant des arguments nommés (keyword arguments). Les arguments nommés vous permettent de spécifier les valeurs des paramètres par leur nom, ce qui peut rendre le code plus lisible. Exécutez la commande suivante :

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

Vous devriez obtenir un message d'erreur comme celui-ci :

```
TypeError: __init__() got an unexpected keyword argument 'name'
```

Cette erreur se produit parce que notre méthode `__init__` actuelle, qui est responsable de l'initialisation des objets de la classe `Stock`, ne gère pas les arguments nommés. Elle n'accepte que les arguments positionnels, ce qui signifie que vous devez fournir les valeurs dans un ordre spécifique sans utiliser les noms de paramètres. C'est une limitation que nous voulons corriger dans ce laboratoire.

Dans ce laboratoire, nous allons explorer différentes approches pour rendre notre classe `Structure` plus flexible et conviviale. En faisant cela, nous pouvons améliorer l'utilisabilité de la classe `Stock` et des autres sous-classes de `Structure`.
