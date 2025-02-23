# Créer un graphique log-log avec limites de données ajustables

Ensuite, nous allons créer un graphique log-log avec des limites de données ajustables. Cela signifie que l'axe des x et l'axe des y auront des échelles logarithmiques, et le rapport d'aspect du graphique sera ajusté pour s'adapter aux données.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_adjustable("datalim")
ax.plot([1, 3, 10], [1, 9, 100], "o-")
ax.set_xlim(1e-1, 1e2)
ax.set_ylim(1e-1, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Datalim")
plt.show()
```
