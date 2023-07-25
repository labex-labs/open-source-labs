# Font Indexing Lab

## Introduction

This lab will guide you through an example of how font tables relate to one another using Python's Matplotlib library.

## Steps

### Step 1: Load the Font

First, we need to load a font file. In this example, we will use DejaVuSans.ttf font file.

```python
import os
import matplotlib
from matplotlib.ft2font import FT2Font

font = FT2Font(os.path.join(matplotlib.get_data_path(), 'fonts/ttf/DejaVuSans.ttf'))
```

### Step 2: Set the Character Map

Next, we set the character map to the standard Unicode character map.

```python
font.set_charmap(0)
```

### Step 3: Get Character Codes and Glyphs

We will get the character codes and corresponding glyphs in the font and store them in two dictionaries, `coded` and `glyphd`.

```python
codes = font.get_charmap().items()

coded = {}
glyphd = {}
for ccode, glyphind in codes:
    name = font.get_glyph_name(glyphind)
    coded[name] = ccode
    glyphd[name] = glyphind
```

### Step 4: Load a Glyph

Now we will load a glyph, the letter 'A', from the font and print its bounding box using the `glyph.bbox` attribute.

```python
code = coded['A']
glyph = font.load_char(code)
print(glyph.bbox)
```

### Step 5: Get Kerning Values

We can get the kerning values between two glyphs by using the `font.get_kerning()` method. In this example, we will get the kerning value between the glyphs for 'A' and 'V' and the glyphs for 'A' and 'T'.

```python
# kerning values for 'AV'
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_DEFAULT))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNFITTED))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNSCALED))

# kerning value for 'AT'
print('AT', font.get_kerning(glyphd['A'], glyphd['T'], KERNING_UNSCALED))
```

## Summary

In this lab, we learned how to load a font file, set the character map, get character codes and glyphs, load a glyph, and get kerning values between glyphs. These are useful techniques for anyone who wants to work with fonts and text in their Python projects.
