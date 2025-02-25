# Personnaliser les étiquettes des axes

Pour personnaliser les étiquettes des axes, nous pouvons utiliser les fonctions `set_xlabel` et `set_ylabel`. Nous pouvons également ajouter des retours à la ligne en utilisant le caractère "\n".

```python
ax0.set_xlabel('this is a xlabel\n(with newlines!)')
ax0.set_ylabel('this is vertical\ntest', multialignment='center')
```
