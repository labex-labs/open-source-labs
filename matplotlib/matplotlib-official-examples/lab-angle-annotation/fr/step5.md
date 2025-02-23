# Montrez différentes positions de texte et unités de taille

```python
fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)
fig.suptitle("Arguments clés d'AngleLabel")
fig.canvas.draw()  # Il est nécessaire de tracer la figure pour définir le renderer

# Montrez différentes positions de texte.
ax1.marges(y=0.4)
ax1.set_title("textposition")
kw = dict(taille=75, unité="points", texte=r"$60°$")

am6 = plot_angle(ax1, (2.0, 0), 60, textposition="à l'intérieur", **kw)
am7 = plot_angle(ax1, (3.5, 0), 60, textposition="à l'extérieur", **kw)
am8 = plot_angle(ax1, (5.0, 0), 60, textposition="bord",
                 text_kw=dict(bbox=dict(boxstyle="arrondi", fc="w")), **kw)
am9 = plot_angle(ax1, (6.5, 0), 60, textposition="bord",
                 text_kw=dict(xytext=(30, 20), arrowprops=dict(arrowstyle="->",
                              connectionstyle="arc3,rad=-0.2")), **kw)

for x, texte in zip([2.0, 3.5, 5.0, 6.5], ['"à l'intérieur"', '"à l'extérieur"', '"bord"',
                                          '"bord", flèche personnalisée']):
    ax1.annotate(texte, xy=(x, 0), xycoords=ax1.get_xaxis_transform(),
                 bbox=dict(boxstyle="arrondi", fc="w"), ha="gauche", taille_de_la_police=8,
                 annotation_clip=True)

# Montrez différentes unités de taille. L'effet de cela peut être observé au mieux
# en modifiant interactivement la taille de la figure
ax2.marges(y=0.4)
ax2.set_title("unité")
kw = dict(texte=r"$60°$", textposition="à l'extérieur")

am10 = plot_angle(ax2, (2.0, 0), 60, taille=50, unité="pixels", **kw)
am11 = plot_angle(ax2, (3.5, 0), 60, taille=50, unité="points", **kw)
am12 = plot_angle(ax2, (5.0, 0), 60, taille=0.25, unité="minimum d'axe", **kw)
am13 = plot_angle(ax2, (6.5, 0), 60, taille=0.25, unité="maximum d'axe", **kw)

for x, texte in zip([2.0, 3.5, 5.0, 6.5], ['"pixels"', '"points"',
                                          '"minimum d'axe"', '"maximum d'axe"']):
    ax2.annotate(texte, xy=(x, 0), xycoords=ax2.get_xaxis_transform(),
                 bbox=dict(boxstyle="arrondi", fc="w"), ha="gauche", taille_de_la_police=8,
                 annotation_clip=True)

plt.show()
```
