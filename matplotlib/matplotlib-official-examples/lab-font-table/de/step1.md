# Drucken von Glyphen in einer Schrift

In diesem Schritt werden wir eine Funktion `print_glyphs` definieren, die alle Glyphen in einer gegebenen Schriftdatei auf die Standardeingabe ausgibt.

```python
import os
import unicodedata
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def print_glyphs(path):
    """
    Druckt alle Glyphen in der gegebenen Schriftdatei auf die Standardeingabe aus.

    Parameter
    ----------
    path : str oder None
        Der Pfad zur Schriftdatei. Wenn None, wird die Standardschrift von Matplotlib verwendet.
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # Die Standardschrift.

    font = FT2Font(path)

    charmap = font.get_charmap()
    max_indices_len = len(str(max(charmap.values())))

    print("Die Schriftart enthält die folgenden Glyphen:")
    for char_code, glyph_index in charmap.items():
        char = chr(char_code)
        name = unicodedata.name(
                char,
                f"{char_code:#x} ({font.get_glyph_name(glyph_index)})")
        print(f"{glyph_index:>{max_indices_len}} {char} {name}")
```
