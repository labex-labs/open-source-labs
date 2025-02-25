# Распечатать глифы в шрифте

В этом шаге мы определим функцию `print_glyphs`, которая выводит все глифы из заданного файла шрифта в стандартный вывод.

```python
import os
import unicodedata
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def print_glyphs(path):
    """
    Print the all glyphs in the given font file to stdout.

    Parameters
    ----------
    path : str or None
        The path to the font file.  If None, use Matplotlib's default font.
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # The default font.

    font = FT2Font(path)

    charmap = font.get_charmap()
    max_indices_len = len(str(max(charmap.values())))

    print("The font face contains the following glyphs:")
    for char_code, glyph_index in charmap.items():
        char = chr(char_code)
        name = unicodedata.name(
                char,
                f"{char_code:#x} ({font.get_glyph_name(glyph_index)})")
        print(f"{glyph_index:>{max_indices_len}} {char} {name}")
```

# Распечатать глифы в шрифте

В этом шаге мы определим функцию `print_glyphs`, которая выводит все глифы из заданного файла шрифта в стандартный вывод.

```python
import os
import unicodedata
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def print_glyphs(path):
    """
    Распечатать все глифы из заданного файла шрифта в стандартный вывод.

    Аргументы
    ----------
    path : str или None
        Путь к файлу шрифта. Если None, использовать стандартный шрифт Matplotlib.
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # Стандартный шрифт.

    font = FT2Font(path)

    charmap = font.get_charmap()
    max_indices_len = len(str(max(charmap.values())))

    print("В этом шрифте содержатся следующие глифы:")
    for char_code, glyph_index in charmap.items():
        char = chr(char_code)
        name = unicodedata.name(
                char,
                f"{char_code:#x} ({font.get_glyph_name(glyph_index)})")
        print(f"{glyph_index:>{max_indices_len}} {char} {name}")
```
