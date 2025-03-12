# Utilisation de `locals()` pour accéder aux arguments d'une fonction

En Python, comprendre les portées (scopes) des variables est crucial. La portée d'une variable détermine où dans le code elle peut être accédée. Python propose une fonction intégrée appelée `locals()` qui est très pratique pour les débutants afin de comprendre la portée des variables. La fonction `locals()` renvoie un dictionnaire contenant toutes les variables locales dans la portée actuelle. Cela peut être extrêmement utile lorsque vous souhaitez inspecter les arguments d'une fonction, car cela vous donne une vue claire des variables disponibles dans une partie spécifique de votre code.

Créons une simple expérience dans l'interpréteur Python pour voir comment cela fonctionne. Tout d'abord, nous devons accéder au répertoire du projet et démarrer l'interpréteur Python. Vous pouvez le faire en exécutant les commandes suivantes dans votre terminal :

```bash
cd ~/project
python3
```

Une fois que vous êtes dans le shell interactif Python, nous allons définir une classe `Stock`. Une classe en Python est comme un modèle pour créer des objets. Dans cette classe, nous allons utiliser la méthode spéciale `__init__`. La méthode `__init__` est un constructeur en Python, ce qui signifie qu'elle est appelée automatiquement lorsqu'un objet de la classe est créé. À l'intérieur de cette méthode `__init__`, nous allons utiliser la fonction `locals()` pour afficher toutes les variables locales.

```python
class Stock:
    def __init__(self, name, shares, price):
        print(locals())
```

Maintenant, créons une instance de cette classe `Stock`. Une instance est un objet réel créé à partir du modèle de la classe. Nous allons passer quelques valeurs pour les paramètres `name`, `shares` et `price`.

```python
s = Stock('GOOG', 100, 490.1)
```

Lorsque vous exécutez ce code, vous devriez voir une sortie similaire à :

```
{'self': <__main__.Stock object at 0x...>, 'name': 'GOOG', 'shares': 100, 'price': 490.1}
```

Cette sortie montre que `locals()` nous donne un dictionnaire contenant toutes les variables locales dans la méthode `__init__`. La référence `self` est une variable spéciale dans les classes Python qui fait référence à l'instance de la classe elle - même. Les autres variables sont les valeurs des paramètres que nous avons passées lors de la création de l'objet `Stock`.

Nous pouvons utiliser cette fonctionnalité de `locals()` pour initialiser automatiquement les attributs d'un objet. Les attributs sont des variables associées à un objet. Définissons une fonction auxiliaire et modifions notre classe `Stock`.

```python
def _init(locs):
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)

class Stock:
    def __init__(self, name, shares, price):
        _init(locals())
```

La fonction `_init` prend le dictionnaire des variables locales obtenu à partir de `locals()`. Elle supprime d'abord la référence `self` du dictionnaire en utilisant la méthode `pop`. Ensuite, elle itère sur les paires clé - valeur restantes dans le dictionnaire et utilise la fonction `setattr` pour définir chaque variable comme un attribut sur l'objet.

Maintenant, testons cette implémentation avec des arguments positionnels et des arguments nommés (keyword arguments). Les arguments positionnels sont passés dans l'ordre dans lequel ils sont définis dans la signature de la fonction, tandis que les arguments nommés sont passés avec les noms de paramètres spécifiés.

```python
# Test with positional arguments
s1 = Stock('GOOG', 100, 490.1)
print(s1.name, s1.shares, s1.price)

# Test with keyword arguments
s2 = Stock(name='AAPL', shares=50, price=125.3)
print(s2.name, s2.shares, s2.price)
```

Les deux approches devraient fonctionner maintenant ! La fonction `_init` nous permet de gérer à la fois les arguments positionnels et les arguments nommés de manière transparente. Elle préserve également les noms de paramètres dans la signature de la fonction, ce qui rend la sortie de la fonction `help()` plus utile. La fonction `help()` en Python fournit des informations sur les fonctions, les classes et les modules, et avoir les noms de paramètres intacts rend ces informations plus significatives.

Une fois que vous avez terminé vos expériences, vous pouvez quitter l'interpréteur Python en exécutant la commande suivante :

```python
exit()
```
