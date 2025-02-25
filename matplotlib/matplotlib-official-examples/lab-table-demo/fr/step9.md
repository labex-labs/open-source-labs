# Ajouter des étiquettes d'axe et un titre

Nous allons ajouter des étiquettes d'axe et un titre au graphique en utilisant les fonctions `plt.ylabel`, `plt.yticks`, `plt.xticks` et `plt.title`.

```python
values = np.arange(0, 2500, 500)
value_increment = 1000

plt.ylabel(f"Perte en {value_increment}'s")
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Perte par catastrophe')
```
