# Créer un graphique

Dans cette étape, vous allez créer le graphique en utilisant les données aléatoires générées précédemment. Plus précisément, vous allez tracer chaque point de données sous forme d'un marqueur avec le symbole de réussite déterminé par la variable de réussite, la taille déterminée par la variable de compétence, la rotation déterminée par la variable d'angle de décollage et la couleur déterminée par la variable de poussée.

```python
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14)
for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))
fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap),
             ax=ax, label="Normalized Thrust [a.u.]")
ax.set_xlabel("X position [m]")
ax.set_ylabel("Y position [m]")
```
