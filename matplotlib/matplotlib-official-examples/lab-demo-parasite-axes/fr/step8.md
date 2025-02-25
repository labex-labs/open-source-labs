# Ajoutez une légende et des couleurs aux axes

Nous ajoutons une légende aux axes hôtes en utilisant la méthode `host.legend()`. Nous définissons également la couleur de l'étiquette de l'axe y gauche des axes hôtes, l'étiquette de l'axe y droit du premier axe parasite et l'étiquette de l'axe y droit du second axe parasite pour qu'elles correspondent respectivement à leurs lignes en utilisant les méthodes `host.axis["left"].label.set_color(p1.get_color())`, `par1.axis["right"].label.set_color(p2.get_color())` et `par2.axis["right2"].label.set_color(p3.get_color())`.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())
```
