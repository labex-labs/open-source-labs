# Dessiner un tableau de caractères

Dans cette étape, nous allons définir une fonction `draw_font_table` qui dessine un tableau de caractères des 255 premiers caractères de la police donnée.

```python
import os
from pathlib import Path
import unicodedata
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def draw_font_table(path):
    """
    Dessine un tableau de caractères des 255 premiers caractères de la police donnée.

    Paramètres
    ----------
    path : str ou None
        Le chemin vers le fichier de police. Si None, utilise la police par défaut de Matplotlib.
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # La police par défaut.

    font = FT2Font(path)

    # Obtenir la table de caractères de la police
    codes = font.get_charmap().items()

    # Créer les étiquettes et les cellules du tableau
    labelc = [f"{i:X}" for i in range(16)]
    labelr = [f"{i:02X}" for i in range(0, 16*16, 16)]
    chars = [["" for c in range(16)] for r in range(16)]

    for char_code, glyph_index in codes:
        if char_code >= 256:
            continue
        row, col = divmod(char_code, 16)
        chars[row][col] = chr(char_code)

    # Dessiner le tableau à l'aide de Axes.table de Matplotlib
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_title(os.path.basename(path))
    ax.set_axis_off()

    table = ax.table(
        cellText=chars,
        rowLabels=labelr,
        colLabels=labelc,
        rowColours=["palegreen"] * 16,
        colColours=["palegreen"] * 16,
        cellColours=[[".95" for c in range(16)] for r in range(16)],
        cellLoc='center',
        loc='upper left',
    )

    # Définir la police des cellules du tableau comme étant la police du chemin donné
    for key, cell in table.get_celld().items():
        row, col = key
        if row > 0 and col > -1:  # Attention à l'indexation particulière du tableau...
            cell.set_text_props(font=Path(path))

    fig.tight_layout()
    plt.show()
```
