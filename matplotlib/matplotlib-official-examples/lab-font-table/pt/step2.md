# Desenhar uma tabela de fontes

Nesta etapa, definiremos uma função `draw_font_table` que desenha uma tabela de fontes dos primeiros 255 caracteres da fonte fornecida.

```python
import os
from pathlib import Path
import unicodedata
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def draw_font_table(path):
    """
    Desenha uma tabela de fontes dos primeiros 255 caracteres da fonte fornecida.

    Parâmetros
    ----------
    path : str ou None
        O caminho para o arquivo de fonte. Se None, use a fonte padrão do Matplotlib.
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # A fonte padrão.

    font = FT2Font(path)

    # Obter o charmap da fonte
    codes = font.get_charmap().items()

    # Criar os rótulos e células da tabela
    labelc = [f"{i:X}" for i in range(16)]
    labelr = [f"{i:02X}" for i in range(0, 16*16, 16)]
    chars = [["" for c in range(16)] for r in range(16)]

    for char_code, glyph_index in codes:
        if char_code >= 256:
            continue
        row, col = divmod(char_code, 16)
        chars[row][col] = chr(char_code)

    # Desenhar a tabela usando Axes.table do Matplotlib
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

    # Definir a fonte das células da tabela para a fonte do caminho fornecido
    for key, cell in table.get_celld().items():
        row, col = key
        if row > 0 and col > -1:  # Cuidado com a indexação idiossincrática da tabela...
            cell.set_text_props(font=Path(path))

    fig.tight_layout()
    plt.show()
```
