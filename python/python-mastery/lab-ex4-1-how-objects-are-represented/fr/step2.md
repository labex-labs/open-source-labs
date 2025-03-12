# Exploration du dictionnaire interne des objets

En Python, les objets sont un concept fondamental. Un objet peut être considéré comme un conteneur qui stocke des données et a certains comportements. L'un des aspects intéressants des objets Python est la manière dont ils stockent leurs attributs. Les attributs sont comme des variables appartenant à un objet. Python stocke ces attributs dans un dictionnaire spécial, accessible via l'attribut `__dict__`. Ce dictionnaire fait partie intégrante de l'objet, et c'est là que Python garde la trace de toutes les données associées à cet objet.

Regardons de plus près cette structure interne en utilisant nos instances `SimpleStock`. En Python, une instance est un objet individuel créé à partir d'une classe. Par exemple, si `SimpleStock` est une classe, `goog` et `ibm` sont des instances de cette classe.

Pour voir le dictionnaire interne de ces instances, nous pouvons utiliser le shell interactif Python. Le shell interactif Python est un excellent outil pour tester rapidement du code et voir les résultats. Dans le shell interactif Python, tapez les commandes suivantes pour inspecter l'attribut `__dict__` de nos instances :

```python
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1}
>>> ibm.__dict__
{'name': 'IBM', 'shares': 50, 'price': 91.23}
```

Lorsque vous exécutez ces commandes, la sortie montre que chaque instance a son propre dictionnaire interne. Ce dictionnaire contient tous les attributs de l'instance. Par exemple, dans l'instance `goog`, les attributs `name`, `shares` et `price` sont stockés dans le dictionnaire avec leurs valeurs correspondantes. C'est ainsi que Python implémente les attributs des objets en coulisse. Chaque objet a un dictionnaire privé qui contient tous ses attributs.

Il est important de comprendre ce que l'attribut `__dict__` révèle sur l'implémentation interne de nos objets :

1. Les clés du dictionnaire correspondent aux noms des attributs. Par exemple, dans l'instance `goog`, la clé `'name'` correspond à l'attribut `name` de l'objet.
2. Les valeurs du dictionnaire sont les valeurs des attributs. Ainsi, la valeur `'GOOG'` est la valeur de l'attribut `name` pour l'instance `goog`.
3. Chaque instance a son propre `__dict__` distinct. Cela signifie que les attributs d'une instance sont indépendants des attributs d'une autre instance. Par exemple, l'attribut `shares` de l'instance `goog` peut être différent de l'attribut `shares` de l'instance `ibm`.

Cette approche basée sur les dictionnaires permet à Python d'être très flexible avec les objets. Comme nous le verrons dans l'étape suivante, nous pouvons utiliser cette flexibilité pour modifier et accéder aux attributs des objets de diverses manières.
