# Créer une figure et un axe

Ensuite, nous allons créer une figure et un axe en utilisant la méthode `subplots()`. Nous allons ensuite tracer deux lignes sur l'axe et ajouter une légende pour les distinguer.

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```
