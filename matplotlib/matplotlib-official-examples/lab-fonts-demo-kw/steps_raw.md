# Matplotlib Fonts Demo Lab

## Introduction

In this lab, we will learn how to set font properties using keyword arguments in Matplotlib. We will explore different font families, styles, variants, weights, and sizes to customize the appearance of our text. We will use Matplotlib's `fig.text()` method to display the different font options.

## Steps

### Step 1: Set up the environment

First, we need to import the necessary libraries and set up the environment by creating a new figure using `plt.figure()`.

```python
import matplotlib.pyplot as plt

fig = plt.figure()
```

### Step 2: Show font families

Next, we will display the different font families available in Matplotlib. We will use the `fig.text()` method to display each font family, with the family name as the text and the corresponding font family as a keyword argument.

```python
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

fig.text(0.1, 0.9, 'family', size='large', **alignment)
families = ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']
for k, family in enumerate(families):
    fig.text(0.1, yp[k], family, family=family, **alignment)
```

### Step 3: Show font styles

Now, we will display the different font styles available in Matplotlib. We will use the `fig.text()` method to display each font style, with the style name as the text and the corresponding font style as a keyword argument.

```python
fig.text(0.3, 0.9, 'style', **alignment)
styles = ['normal', 'italic', 'oblique']
for k, style in enumerate(styles):
    fig.text(0.3, yp[k], style, family='sans-serif', style=style, **alignment)
```

### Step 4: Show font variants

Next, we will display the different font variants available in Matplotlib. We will use the `fig.text()` method to display each font variant, with the variant name as the text and the corresponding font variant as a keyword argument.

```python
fig.text(0.5, 0.9, 'variant', **alignment)
variants = ['normal', 'small-caps']
for k, variant in enumerate(variants):
    fig.text(0.5, yp[k], variant, family='serif', variant=variant, **alignment)
```

### Step 5: Show font weights

Now, we will display the different font weights available in Matplotlib. We will use the `fig.text()` method to display each font weight, with the weight name as the text and the corresponding font weight as a keyword argument.

```python
fig.text(0.7, 0.9, 'weight', **alignment)
weights = ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
for k, weight in enumerate(weights):
    fig.text(0.7, yp[k], weight, weight=weight, **alignment)
```

### Step 6: Show font sizes

Finally, we will display the different font sizes available in Matplotlib. We will use the `fig.text()` method to display each font size, with the size name as the text and the corresponding font size as a keyword argument.

```python
fig.text(0.9, 0.9, 'size', **alignment)
sizes = [
    'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']
for k, size in enumerate(sizes):
    fig.text(0.9, yp[k], size, size=size, **alignment)
```

### Step 7: Show bold italic

As a bonus, we can also display text with both bold and italic styles. We will use the `fig.text()` method to display the text with the appropriate style, weight, and size.

```python
fig.text(0.3, 0.1, 'bold italic',
         style='italic', weight='bold', size='x-small', **alignment)
fig.text(0.3, 0.2, 'bold italic',
         style='italic', weight='bold', size='medium', **alignment)
fig.text(0.3, 0.3, 'bold italic',
         style='italic', weight='bold', size='x-large', **alignment)
```

## Summary

In this lab, we learned how to set font properties using keyword arguments in Matplotlib. We explored different font families, styles, variants, weights, and sizes to customize the appearance of our text. We used the `fig.text()` method to display the different font options.
