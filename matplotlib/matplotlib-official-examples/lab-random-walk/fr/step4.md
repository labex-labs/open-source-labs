# Générer des mouvements aléatoires

Nous générons 40 mouvements aléatoires avec 30 pas chacun à l'aide de la fonction `random_walk()` définie précédemment. Nous stockons tous les mouvements aléatoires dans une liste appelée `walks`.

```python
# Données : 40 mouvements aléatoires sous forme de tableaux (num_steps, 3)
num_steps = 30
walks = [random_walk(num_steps) for index in range(40)]
```
