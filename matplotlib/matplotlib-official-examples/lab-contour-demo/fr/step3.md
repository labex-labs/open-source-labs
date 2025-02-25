# Créer un graphe de niveau simple avec étiquettes

Maintenant que nous avons nos données, nous pouvons créer un graphe de niveau simple avec des étiquettes en utilisant les couleurs par défaut.

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simplest default with labels')
```
