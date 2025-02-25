# Dibujar una tabla de fuentes

En este paso, definiremos una función `draw_font_table` que dibuja una tabla de fuentes de los primeros 255 caracteres de la fuente dada.

```python
import os
from pathlib import Path
import unicodedata
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def draw_font_table(path):
    """
    Dibuja una tabla de fuentes de los primeros 255 caracteres de la fuente dada.

    Parámetros
    ----------
    path : str o None
        La ruta al archivo de fuente. Si es None, se utiliza la fuente predeterminada de Matplotlib.
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # La fuente predeterminada.

    font = FT2Font(path)

    # Obtiene el mapa de caracteres de la fuente
    codes = font.get_charmap().items()

    # Crea las etiquetas y celdas de la tabla
    labelc = [f"{i:X}" for i in range(16)]
    labelr = [f"{i:02X}" for i in range(0, 16*16, 16)]
    chars = [["" for c in range(16)] for r in range(16)]

    for char_code, glyph_index in codes:
        if char_code >= 256:
            continue
        row, col = divmod(char_code, 16)
        chars[row][col] = chr(char_code)

    # Dibuja la tabla utilizando Axes.table de Matplotlib
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

    # Establece la fuente de las celdas de la tabla a la fuente de la ruta dada
    for key, cell in table.get_celld().items():
        row, col = key
        if row > 0 and col > -1:  # Tenga cuidado con la indexación idiosincrática de la tabla...
            cell.set_text_props(font=Path(path))

    fig.tight_layout()
    plt.show()
```
