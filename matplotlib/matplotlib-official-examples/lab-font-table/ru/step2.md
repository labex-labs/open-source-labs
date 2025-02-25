# Нарисовать таблицу шрифта

В этом шаге мы определим функцию `draw_font_table`, которая рисует таблицу шрифта первых 255 символов заданного шрифта.

```python
import os
from pathlib import Path
import unicodedata
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def draw_font_table(path):
    """
    Нарисовать таблицу шрифта первых 255 символов заданного шрифта.

    Параметры
    ----------
    path : str или None
        Путь к файлу шрифта. Если None, использовать стандартный шрифт Matplotlib.
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # Стандартный шрифт.

    font = FT2Font(path)

    # Получить карту символов шрифта
    codes = font.get_charmap().items()

    # Создать метки и ячейки таблицы
    labelc = [f"{i:X}" for i in range(16)]
    labelr = [f"{i:02X}" for i in range(0, 16*16, 16)]
    chars = [["" for c in range(16)] for r in range(16)]

    for char_code, glyph_index in codes:
        if char_code >= 256:
            continue
        row, col = divmod(char_code, 16)
        chars[row][col] = chr(char_code)

    # Нарисовать таблицу с использованием Axes.table Matplotlib
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

    # Установить шрифт ячеек таблицы равным шрифту заданного пути
    for key, cell in table.get_celld().items():
        row, col = key
        if row > 0 and col > -1:  # Будьте осторожны с необычным индексированием таблицы...
            cell.set_text_props(font=Path(path))

    fig.tight_layout()
    plt.show()
```
