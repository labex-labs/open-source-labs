# Trouver les anomalies de parité

## Problème

Écrivez une fonction `find_parity_outliers(nums)` qui prend une liste d'entiers `nums` en argument et renvoie une liste de tous les éléments ayant une parité différente de la majorité dans `nums`.

Pour résoudre ce problème, vous pouvez suivre les étapes suivantes :

1. Utilisez `collections.Counter` avec une compréhension de liste pour compter les valeurs paires et impaires dans la liste.
2. Utilisez `collections.Counter.most_common()` pour obtenir la parité la plus fréquente.
3. Utilisez une compréhension de liste pour trouver tous les éléments qui ne correspondent pas à la parité la plus fréquente.

## Exemple

```python
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```

Dans l'exemple ci-dessus, la majorité des éléments de la liste sont pairs, donc les anomalies de parité sont les éléments impairs 1 et 3.
