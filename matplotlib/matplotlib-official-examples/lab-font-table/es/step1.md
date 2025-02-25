# Imprimir los glifos de una fuente

En este paso, definiremos una función `print_glyphs` que imprime todos los glifos de un archivo de fuente dado a la salida estándar.

```python
import os
import unicodedata
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def print_glyphs(path):
    """
    Imprime todos los glifos del archivo de fuente dado a la salida estándar.

    Parámetros
    ----------
    path : str o None
        La ruta al archivo de fuente. Si es None, se utiliza la fuente predeterminada de Matplotlib.
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # La fuente predeterminada.

    font = FT2Font(path)

    charmap = font.get_charmap()
    max_indices_len = len(str(max(charmap.values())))

    print("La fuente contiene los siguientes glifos:")
    for char_code, glyph_index in charmap.items():
        char = chr(char_code)
        name = unicodedata.name(
                char,
                f"{char_code:#x} ({font.get_glyph_name(glyph_index)})")
        print(f"{glyph_index:>{max_indices_len}} {char} {name}")
```
