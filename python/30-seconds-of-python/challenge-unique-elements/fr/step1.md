# Éléments uniques dans une liste

## Problème

Écrivez une fonction Python appelée `unique_elements` qui prend une liste en entrée et renvoie une nouvelle liste ne contenant que les éléments uniques. Votre fonction doit effectuer les étapes suivantes :

- Créez un `ensemble` à partir de la liste pour éliminer les valeurs dupliquées.
- Retournez une `liste` à partir de l'ensemble.

Votre fonction devrait avoir la signature suivante :

```python
def unique_elements(li: List) -> List:
```

## Exemple

```python
assert unique_elements([1, 2, 2, 3, 4, 3]) == [1, 2, 3, 4]
assert unique_elements(['a', 'b', 'c', 'a', 'd']) == ['a', 'b', 'c', 'd']
assert unique_elements([]) == []
```
