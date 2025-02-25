# Créer une fonction pour définir les paramètres par défaut

Pour créer une fonction qui définit les paramètres par défaut pour vos figures, vous pouvez utiliser la méthode `rcParams.update()`. Cette méthode prend un dictionnaire de noms et de valeurs de paramètres, et met à jour les valeurs par défaut actuelles avec les nouvelles. Voici un exemple d'une fonction qui définit certains paramètres par défaut pour les figures destinées à la publication :

```python
def set_pub():
    rcParams.update({
        "font.weight": "bold",  # police en gras
        "tick.labelsize": 15,   # étiquettes d'échelle de grande taille
        "lines.linewidth": 1,   # lignes épaisse
        "lines.color": "k",     # lignes noires
        "grid.color": "0.5",    # lignes de grille grises
        "grid.linestyle": "-",  # lignes de grille solides
        "grid.linewidth": 0.5,  # lignes de grille fines
        "savefig.dpi": 300,     # sortie à une résolution plus élevée.
    })
```
