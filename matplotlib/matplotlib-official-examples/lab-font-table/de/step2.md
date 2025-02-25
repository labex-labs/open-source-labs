# Zeichnen einer Schrifttabelle

In diesem Schritt werden wir eine Funktion `draw_font_table` definieren, die eine Schrifttabelle der ersten 255 Zeichen der gegebenen Schrift zeichnet.

```python
import os
from pathlib import Path
import unicodedata
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def draw_font_table(path):
    """
    Zeichnet eine Schrifttabelle der ersten 255 Zeichen der gegebenen Schrift.

    Parameter
    ----------
    path : str oder None
        Der Pfad zur Schriftdatei. Wenn None, wird die Standardschrift von Matplotlib verwendet.
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # Die Standardschrift.

    font = FT2Font(path)

    # Holt die Zeichenkarte der Schrift
    codes = font.get_charmap().items()

    # Erstellt die Labels und Zellen der Tabelle
    labelc = [f"{i:X}" for i in range(16)]
    labelr = [f"{i:02X}" for i in range(0, 16*16, 16)]
    chars = [["" for c in range(16)] for r in range(16)]

    for char_code, glyph_index in codes:
        if char_code >= 256:
            continue
        row, col = divmod(char_code, 16)
        chars[row][col] = chr(char_code)

    # Zeichnet die Tabelle mit Hilfe von Matplotlib's Axes.table
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

    # Setzt die Schrift der Tabellenzellen auf die Schrift des gegebenen Pfads
    for key, cell in table.get_celld().items():
        row, col = key
        if row > 0 and col > -1:  # Achten Sie auf die eigenartige Indizierung der Tabelle...
            cell.set_text_props(font=Path(path))

    fig.tight_layout()
    plt.show()
```
