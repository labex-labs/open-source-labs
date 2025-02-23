# Créer un graphique log-log avec boîte ajustable

Ensuite, nous allons créer un graphique log-log avec une boîte ajustable. Cela signifie que l'axe des x et l'axe des y auront des échelles logarithmiques, et le rapport d'aspect du graphique sera égal à 1.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e1, 1e3)
ax.set_ylim(1e2, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Box")
plt.show()
```
