# Créer le graphique

Créez un objet figure et d'axe à l'aide de `subplots`. Tracez les valeurs de x et de y à l'aide de `plot`. Réglez les limites de l'axe y pour commencer à 0 à l'aide de `set_ylim`.

```python
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)
```
