# Afficher les glyphes d'une police

Dans cette étape, nous allons définir une fonction `print_glyphs` qui affiche tous les glyphes d'un fichier de police donné sur la sortie standard.

```python
import os
import unicodedata
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def print_glyphs(path):
    """
    Affiche tous les glyphes du fichier de police donné sur la sortie standard.

    Paramètres
    ----------
    path : str ou None
        Le chemin vers le fichier de police. Si None, utilise la police par défaut de Matplotlib.
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # La police par défaut.

    font = FT2Font(path)

    charmap = font.get_charmap()
    max_indices_len = len(str(max(charmap.values())))

    print("La police contient les glyphes suivants :")
    for char_code, glyph_index in charmap.items():
        char = chr(char_code)
        name = unicodedata.name(
                char,
                f"{char_code:#x} ({font.get_glyph_name(glyph_index)})")
        print(f"{glyph_index:>{max_indices_len}} {char} {name}")
```
