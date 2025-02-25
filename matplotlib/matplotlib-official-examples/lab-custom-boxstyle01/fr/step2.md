# Implémenter un style de boîte personnalisé sous forme de classe

Les styles de boîte personnalisés peuvent également être implémentés sous forme de classes qui implémentent `__call__`. Les classes peuvent ensuite être enregistrées dans le dictionnaire `BoxStyle._style_list`, ce qui permet de spécifier le style de boîte sous forme de chaîne de caractères, `bbox=dict(boxstyle="nom_enregistré,param=valeur,...",...)`.

```python
class MyStyle:
    """Une simple boîte."""

    def __init__(self, pad=0.3):
        """
        Les arguments doivent être des nombres flottants et avoir des valeurs par défaut.

        Paramètres
        ----------
        pad : float
            Quantité de padding
        """
        self.pad = pad
        super().__init__()

    def __call__(self, x0, y0, width, height, mutation_size):
        """
        Étant donné l'emplacement et la taille de la boîte, renvoie le chemin de la boîte
        autour de celle-ci.

        La rotation est automatiquement prise en compte.

        Paramètres
        ----------
        x0, y0, width, height : float
            Emplacement et taille de la boîte.
        mutation_size : float
            Échelle de référence pour la mutation, généralement la taille de police du texte.
        """
        # padding
        pad = mutation_size * self.pad
        # largeur et hauteur avec padding ajouté
        width = width + 2.*pad
        height = height + 2.*pad
        # limite de la boîte avec padding
        x0, y0 = x0 - pad, y0 - pad
        x1, y1 = x0 + width, y0 + height
        # renvoie le nouveau chemin
        return Path([(x0, y0),
                     (x1, y0), (x1, y1), (x0, y1),
                     (x0-pad, (y0+y1)/2.), (x0, y0),
                     (x0, y0)],
                    closed=True)


BoxStyle._style_list["angled"] = MyStyle  # Enregistre le style personnalisé.

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))

del BoxStyle._style_list["angled"]  # Désenregistre-le.

plt.show()
```
