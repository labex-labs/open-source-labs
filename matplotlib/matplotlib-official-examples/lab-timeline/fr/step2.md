# Création d'un diagramme en tiges

Ensuite, nous allons créer un diagramme en tiges avec quelques variations de niveau pour distinguer même des événements proches. Nous ajoutons des marqueurs sur la ligne de base pour souligner visuellement la nature unidimensionnelle de la chronologie. Pour chaque événement, nous ajoutons une étiquette de texte via `~.Axes.annotate`, qui est décalée en points à partir de la pointe de la ligne de l'événement. Voici le code pour créer un diagramme en tiges :

```python
# Choisissez quelques niveaux agréables
levels = np.tile([-5, 5, -3, 3, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# Créez une figure et tracez un diagramme en tiges avec la date
fig, ax = plt.subplots(figsize=(8.8, 4), layout="constrained")
ax.set(title="Matplotlib release dates")

ax.vlines(dates, 0, levels, color="tab:red")  # Les tiges verticales.
ax.plot(dates, np.zeros_like(dates), "-o",
        color="k", markerfacecolor="w")  # La ligne de base et les marqueurs dessus.

# annoter les lignes
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")
```
