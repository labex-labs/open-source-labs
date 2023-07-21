# Font Properties Lab

## Introduction

In this lab, you will learn about the attributes of an `.FT2Font` object that describe global font properties. You will also learn how to use individual character metrics using the `.Glyph` object, as returned by `.load_char`.

## Steps

### Step 1: Import necessary libraries

In this step, we will import the necessary libraries.

```python
import os
import matplotlib
import matplotlib.ft2font as ft
```

### Step 2: Load Font

In this step, we will load the font that we will be working with. We will use a font shipped with Matplotlib.

```python
font = ft.FT2Font(
    os.path.join(matplotlib.get_data_path(),
                 'fonts/ttf/DejaVuSans-Oblique.ttf'))
```

### Step 3: Print Font Properties

In this step, we will print the properties of the font.

```python
print('Num faces:  ', font.num_faces)        # number of faces in file
print('Num glyphs: ', font.num_glyphs)       # number of glyphs in the face
print('Family name:', font.family_name)      # face family name
print('Style name: ', font.style_name)       # face style name
print('PS name:    ', font.postscript_name)  # the postscript name
print('Num fixed:  ', font.num_fixed_sizes)  # number of embedded bitmaps
```

### Step 4: Print Additional Font Properties

In this step, we will print additional font properties that are only available if the face is scalable.

```python
if font.scalable:
    # the face global bounding box (xmin, ymin, xmax, ymax)
    print('Bbox:               ', font.bbox)
    # number of font units covered by the EM
    print('EM:                 ', font.units_per_EM)
    # the ascender in 26.6 units
    print('Ascender:           ', font.ascender)
    # the descender in 26.6 units
    print('Descender:          ', font.descender)
    # the height in 26.6 units
    print('Height:             ', font.height)
    # maximum horizontal cursor advance
    print('Max adv width:      ', font.max_advance_width)
    # same for vertical layout
    print('Max adv height:     ', font.max_advance_height)
    # vertical position of the underline bar
    print('Underline pos:      ', font.underline_position)
    # vertical thickness of the underline
    print('Underline thickness:', font.underline_thickness)
```

### Step 5: Print Font Styles

In this step, we will print the font styles.

```python
for style in ('Italic',
              'Bold',
              'Scalable',
              'Fixed sizes',
              'Fixed width',
              'SFNT',
              'Horizontal',
              'Vertical',
              'Kerning',
              'Fast glyphs',
              'Multiple masters',
              'Glyph names',
              'External stream'):
    bitpos = getattr(ft, style.replace(' ', '_').upper()) - 1
    print(f"{style+':':17}", bool(font.style_flags & (1 << bitpos)))
```

## Summary

In this lab, you learned about the attributes of an `.FT2Font` object that describe global font properties. You also learned how to use individual character metrics using the `.Glyph` object, as returned by `.load_char`.
