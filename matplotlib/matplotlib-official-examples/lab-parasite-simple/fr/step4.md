# Ajout des données

Nous allons ajouter les données au graphique en utilisant la fonction `plot`. Nous allons assigner chaque ligne à une variable afin que nous puissions y faire référence plus tard.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Densité")
p2, = par.plot([0, 1, 2], [0, 3, 2], label="Température")
```
