# Tracez deux lignes qui se croisent et étiquetez chaque angle entre elles avec l'outil `AngleAnnotation` ci-dessus.

```python
fig, ax = plt.subplots()
fig.canvas.draw()  # Il est nécessaire de tracer la figure pour définir le renderer
ax.set_title("Exemple d'AngleLabel")

# Tracez deux lignes qui se croisent et étiquetez chaque angle entre elles avec l'outil
# ``AngleAnnotation`` ci-dessus.
centre = (4.5, 650)
p1 = [(2.5, 710), (6.0, 605)]
p2 = [(3.0, 275), (5.5, 900)]
ligne1, = ax.plot(*zip(*p1))
ligne2, = ax.plot(*zip(*p2))
point, = ax.plot(*centre, marqueur="o")

am1 = AngleAnnotation(centre, p1[1], p2[1], ax=ax, taille=75, texte=r"$\alpha$")
am2 = AngleAnnotation(centre, p2[1], p1[0], ax=ax, taille=35, texte=r"$\beta$")
am3 = AngleAnnotation(centre, p1[0], p2[0], ax=ax, taille=75, texte=r"$\gamma$")
am4 = AngleAnnotation(centre, p2[0], p1[1], ax=ax, taille=35, texte=r"$\theta$")


# Montrez quelques options de style pour l'arc d'angle, ainsi que le texte.
p = [(6.0, 400), (5.3, 410), (5.6, 300)]
ax.plot(*zip(*p))
am5 = AngleAnnotation(p[1], p[0], p[2], ax=ax, taille=40, texte=r"$\Phi$",
                      style_de_ligne="--", couleur="gris", position_du_texte="à l'extérieur",
                      kw_du_texte=dict(taille_de_la_police=16, couleur="gris"))

plt.show()
```
