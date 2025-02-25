# Définir les limites x en utilisant des scalaires ou des unités

Dans cette étape, nous allons définir les limites x en utilisant des scalaires ou des unités. Nous utiliserons la méthode `set_xlim` pour définir les limites x. Nous définirons les limites x à 2 et 6 en utilisant des scalaires dans les unités actuelles pour le graphique en barres dans la deuxième ligne et la première colonne. Nous définirons les limites x à 2 cm et 6 cm en utilisant des unités pour le graphique en barres dans la deuxième ligne et la deuxième colonne.

```python
axs[1, 0].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(2, 6)

axs[1, 1].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(2 * cm, 6 * cm)
```
