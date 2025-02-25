# Créer un graphique

Ensuite, nous allons créer un graphique simple pour démontrer les différents options de `CapStyle`.

```python
fig, ax = plt.subplots()

# Tracer la ligne avec différentes options de CapStyle
for i, cap_style in enumerate(CapStyle):
    ax.plot([0, 1], [i, i], label=str(cap_style), linewidth=10, solid_capstyle=cap_style)

# Ajouter une légende et un titre
ax.legend(title='CapStyle')
ax.set_title('CapStyle Demo')
```
