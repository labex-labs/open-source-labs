# Ways to Set a Color's Alpha Value

## Introduction

This lab is about setting a color's alpha value using the Python Matplotlib library. Alpha value is a measure of transparency, where a value of 0 means completely transparent and a value of 1 means completely opaque. We will explore two ways to set alpha value in Matplotlib: using the `alpha` keyword argument and using the `(matplotlib_color, alpha)` color format.

## Steps

### Step 1: Creating a Bar Chart with Explicit Alpha Value

In this step, we will create a bar chart using the `bar` method in Matplotlib. We will set the alpha value using the `alpha` keyword argument. All bars in the chart will have the same alpha value.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility.
np.random.seed(19680801)

fig, ax = plt.subplots()

x_values = [n for n in range(20)]
y_values = np.random.randn(20)

facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors

ax.bar(x_values, y_values, color=facecolors, edgecolor=edgecolors, alpha=0.5)
ax.set_title("Explicit 'alpha' keyword value\nshared by all bars and edges")

plt.show()
```

### Step 2: Creating a Bar Chart with Varying Alpha Values

In this step, we will create a bar chart using the `bar` method in Matplotlib. We will set the alpha value using the `(matplotlib_color, alpha)` color format. Each bar in the chart will have a different alpha value, based on its y-value.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility.
np.random.seed(19680801)

fig, ax = plt.subplots()

x_values = [n for n in range(20)]
y_values = np.random.randn(20)

facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors

# Normalize y values to get distinct face alpha values.
abs_y = [abs(y) for y in y_values]
face_alphas = [n / max(abs_y) for n in abs_y]
edge_alphas = [1 - alpha for alpha in face_alphas]

colors_with_alphas = list(zip(facecolors, face_alphas))
edgecolors_with_alphas = list(zip(edgecolors, edge_alphas))

ax.bar(x_values, y_values, color=colors_with_alphas,
        edgecolor=edgecolors_with_alphas)
ax.set_title('Normalized alphas for\neach bar and each edge')

plt.show()
```

## Summary

In this lab, we learned two ways to set a color's alpha value in Matplotlib: using the `alpha` keyword argument and using the `(matplotlib_color, alpha)` color format. The `alpha` keyword argument sets the same alpha value for all bars in a chart, while the `(matplotlib_color, alpha)` color format allows us to set different alpha values for each bar based on its y-value.
