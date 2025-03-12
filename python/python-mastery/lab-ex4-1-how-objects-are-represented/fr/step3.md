# Ajout et modification d'attributs d'objet

En Python, les objets sont implémentés sur la base de dictionnaires. Cette implémentation confère à Python un haut degré de flexibilité lorsqu'il s'agit de gérer les attributs des objets. Contrairement à certains autres langages de programmation, Python ne limite pas les attributs d'un objet aux seuls attributs définis dans sa classe. Cela signifie que vous pouvez ajouter de nouveaux attributs à un objet à tout moment, même après sa création.

Explorons cette flexibilité en ajoutant un nouvel attribut à l'une de nos instances. Supposons que nous ayons une instance nommée `goog` d'une classe. Nous allons lui ajouter un attribut `date` :

```python
>>> goog.date = "6/11/2007"
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1, 'date': '6/11/2007'}
```

Ici, nous avons ajouté un nouvel attribut `date` à l'instance `goog`. Notez que cet attribut `date` n'était pas défini dans la classe `SimpleStock`. Ce nouvel attribut n'existe que sur l'instance `goog`. Pour confirmer cela, vérifions l'instance `ibm` :

```python
>>> ibm.__dict__
{'name': 'IBM', 'shares': 50, 'price': 91.23}
>>> hasattr(ibm, 'date')
False
```

Comme nous pouvons le voir, l'instance `ibm` n'a pas l'attribut `date`. Cela montre trois caractéristiques importantes des objets Python :

1. Chaque instance a son propre ensemble unique d'attributs.
2. Les attributs peuvent être ajoutés à un objet après sa création.
3. L'ajout d'un attribut à une instance n'affecte pas les autres instances.

Maintenant, essayons une autre façon d'ajouter un attribut. Au lieu d'utiliser la notation par point, nous allons manipuler directement le dictionnaire sous - jacent de l'objet. En Python, chaque objet a un attribut spécial `__dict__` qui stocke tous ses attributs sous forme de paires clé - valeur.

```python
>>> goog.__dict__['time'] = '9:45am'
>>> goog.time
'9:45am'
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1, 'date': '6/11/2007', 'time': '9:45am'}
```

En modifiant directement le dictionnaire `__dict__`, nous avons ajouté un nouvel attribut `time` à l'instance `goog`. Lorsque nous accédons à `goog.time`, Python cherche la clé 'time' dans le dictionnaire `__dict__` et renvoie sa valeur correspondante.

Ces exemples illustrent que les objets Python sont essentiellement des dictionnaires avec quelques fonctionnalités supplémentaires. La flexibilité des objets Python permet des modifications dynamiques, ce qui est très puissant et pratique en programmation.
