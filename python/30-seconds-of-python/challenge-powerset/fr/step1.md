# Défi de l'ensemble des parties

## Problème

Écrire une fonction Python appelée `powerset(iterable)` qui prend un itérable en argument et renvoie l'ensemble des parties de l'itérable. La fonction doit suivre les étapes suivantes :

1. Convertir la valeur donnée en une liste.
2. Utiliser `range()` et `itertools.combinations()` pour créer un générateur qui renvoie tous les sous-ensembles.
3. Utiliser `itertools.chain.from_iterable()` et `list()` pour consommer le générateur et renvoyer une liste.

## Exemple

```python
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]
```
