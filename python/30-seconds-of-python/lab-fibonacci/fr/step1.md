# Fibonacci

Écrivez une fonction appelée `fibonacci(n)` qui prend un entier `n` comme paramètre et renvoie une liste contenant la suite de Fibonacci jusqu'au n-ième terme.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Créez une liste vide appelée `sequence`.
2. Si `n` est inférieur ou égal à 0, ajoutez 0 à la liste `sequence` et renvoyez la liste.
3. Ajoutez 0 et 1 à la liste `sequence`.
4. Utilisez une boucle `while` pour ajouter la somme des deux derniers nombres de la liste `sequence` à la fin de la liste, jusqu'à ce que la longueur de la liste atteigne `n`.
5. Renvoyez la liste `sequence`.

```python
def fibonacci(n):
  if n <= 0:
    return [0]
  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)
  return sequence
```

```python
fibonacci(7) # [0, 1, 1, 2, 3, 5, 8, 13]
```
