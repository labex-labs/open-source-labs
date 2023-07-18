# Font Table Tutorial

## Introduction

Matplotlib is a popular data visualization library in Python. It provides font support through the FreeType library. In this lab, we will learn how to draw a font table of the first 255 characters of a given font using Matplotlib's `Axes.table`.

## Steps

### Step 1: Print the glyphs in a font

In this step, we will define a function `print_glyphs` that prints all the glyphs in a given font file to stdout.

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

### Step 2: Draw a font table

In this step, we will define a function `draw_font_table` that draws a font table of the first 255 characters of the given font.

```python
import os
from pathlib import Path
import unicodedata
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def draw_font_table(path):
    """
    Draw a font table of the first 255 chars of the given font.

    Parameters
    ----------
    path : str or None
        The path to the font file.  If None, use Matplotlib's default font.
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # The default font.

    font = FT2Font(path)

    # Get the charmap of the font
    codes = font.get_charmap().items()

    # Create the labels and cells of the table
    labelc = [f"{i:X}" for i in range(16)]
    labelr = [f"{i:02X}" for i in range(0, 16*16, 16)]
    chars = [["" for c in range(16)] for r in range(16)]

    for char_code, glyph_index in codes:
        if char_code >= 256:
            continue
        row, col = divmod(char_code, 16)
        chars[row][col] = chr(char_code)

    # Draw the table using Matplotlib's Axes.table
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

    # Set the font of the table cells to the font of the given path
    for key, cell in table.get_celld().items():
        row, col = key
        if row > 0 and col > -1:  # Beware of table's idiosyncratic indexing...
            cell.set_text_props(font=Path(path))

    fig.tight_layout()
    plt.show()
```

### Step 3: Display the font table

In this step, we will use `argparse` to parse the path to the font file from the command-line arguments. Then we will call `print_glyphs` to print all the glyphs in the font file, and `draw_font_table` to draw the font table of the first 255 characters of the font.

```python
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Display a font table.")
    parser.add_argument("path", nargs="?", help="Path to the font file.")
    parser.add_argument("--print-all", action="store_true",
                        help="Additionally, print all chars to stdout.")
    args = parser.parse_args()

    if args.print_all:
        print_glyphs(args.path)
    draw_font_table(args.path)
```

## Summary

In this lab, we learned how to draw a font table of the first 255 characters of a font file using Matplotlib's `Axes.table`. We defined functions to print all the glyphs in a font file and to draw the font table. We also used `argparse` to parse the path to the font file from the command-line arguments.
