# Matplotlib Fonts Demo Lab

## Introduction

In this lab, you will learn how to use different font properties in Matplotlib to enhance the visual appearance of your plots.

## Steps

### Step 1: Set Up

Before we get started, we need to import the necessary libraries and set up the plot.

```python
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fig = plt.figure()
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]
heading_font = FontProperties(size='large')
```

### Step 2: Family Options

The first font property we will explore is the family option. This property allows you to set the font family used in your plot.

```python
# Show family options
fig.text(0.1, 0.9, 'family', fontproperties=heading_font, **alignment)
families = ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']
for k, family in enumerate(families):
    font = FontProperties()
    font.set_family(family)
    fig.text(0.1, yp[k], family, fontproperties=font, **alignment)
```

### Step 3: Style Options

The second font property we will explore is the style option. This property allows you to set the font style used in your plot.

```python
# Show style options
styles = ['normal', 'italic', 'oblique']
fig.text(0.3, 0.9, 'style', fontproperties=heading_font, **alignment)
for k, style in enumerate(styles):
    font = FontProperties()
    font.set_family('sans-serif')
    font.set_style(style)
    fig.text(0.3, yp[k], style, fontproperties=font, **alignment)
```

### Step 4: Variant Options

The third font property we will explore is the variant option. This property allows you to set the font variant used in your plot.

```python
# Show variant options
variants = ['normal', 'small-caps']
fig.text(0.5, 0.9, 'variant', fontproperties=heading_font, **alignment)
for k, variant in enumerate(variants):
    font = FontProperties()
    font.set_family('serif')
    font.set_variant(variant)
    fig.text(0.5, yp[k], variant, fontproperties=font, **alignment)
```

### Step 5: Weight Options

The fourth font property we will explore is the weight option. This property allows you to set the font weight used in your plot.

```python
# Show weight options
weights = ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
fig.text(0.7, 0.9, 'weight', fontproperties=heading_font, **alignment)
for k, weight in enumerate(weights):
    font = FontProperties()
    font.set_weight(weight)
    fig.text(0.7, yp[k], weight, fontproperties=font, **alignment)
```

### Step 6: Size Options

The fifth font property we will explore is the size option. This property allows you to set the font size used in your plot.

```python
# Show size options
sizes = [
    'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']
fig.text(0.9, 0.9, 'size', fontproperties=heading_font, **alignment)
for k, size in enumerate(sizes):
    font = FontProperties()
    font.set_size(size)
    fig.text(0.9, yp[k], size, fontproperties=font, **alignment)
```

### Step 7: Bold Italic

The final font property we will explore is a combination of the style and weight options. This property allows you to set the font style and weight used in your plot.

```python
# Show bold italic
font = FontProperties(style='italic', weight='bold', size='x-small')
fig.text(0.3, 0.1, 'bold italic', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='medium')
fig.text(0.3, 0.2, 'bold italic', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='x-large')
fig.text(0.3, 0.3, 'bold italic', fontproperties=font, **alignment)
```

## Summary

In this lab, you learned how to use different font properties in Matplotlib to enhance the visual appearance of your plots. By setting the font family, style, variant, weight, and size, you can customize your plot's font to fit your specific needs.
