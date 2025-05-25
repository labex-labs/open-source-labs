# Imprimir os glifos em uma fonte

Nesta etapa, definiremos uma função `print_glyphs` que imprime todos os glifos em um determinado arquivo de fonte para a saída padrão (stdout).

```python
import os
import unicodedata
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def print_glyphs(path):
    """
    Imprime todos os glifos no arquivo de fonte fornecido para a saída padrão.

    Parâmetros
    ----------
    path : str ou None
        O caminho para o arquivo de fonte. Se None, use a fonte padrão do Matplotlib.
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # A fonte padrão.

    font = FT2Font(path)

    charmap = font.get_charmap()
    max_indices_len = len(str(max(charmap.values())))

    print("A face da fonte contém os seguintes glifos:")
    for char_code, glyph_index in charmap.items():
        char = chr(char_code)
        name = unicodedata.name(
                char,
                f"{char_code:#x} ({font.get_glyph_name(glyph_index)})")
        print(f"{glyph_index:>{max_indices_len}} {char} {name}")
```
