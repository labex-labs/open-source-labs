# Formatage des étiquettes de l'axe des ordonnées avec des signes dollars

Maintenant, formattons les étiquettes de l'axe des ordonnées (y-axis) pour afficher des signes dollars. Nous allons utiliser la classe `StrMethodFormatter` du module `matplotlib.ticker` pour formater les étiquettes.

```python
import matplotlib.ticker as ticker

# Format y-axis labels with dollar signs
fmt = '${x:,.2f}'
tick = ticker.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
```

Dans le code ci-dessus, nous créons un objet `StrMethodFormatter` avec la chaîne de format `'${x:,.2f}'`. Cette chaîne de format spécifie que nous voulons un signe dollar suivi d'un espace, puis d'un nombre séparé par des virgules avec deux décimales.

Ensuite, nous créons un objet `Tick` en utilisant l'objet `StrMethodFormatter` que nous venons de créer. Enfin, nous définissons le formateur principal de l'axe des ordonnées sur l'objet `Tick`.
