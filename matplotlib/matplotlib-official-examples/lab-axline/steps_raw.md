# Matplotlib Tutorial

## Introduction

Matplotlib is a Python library used to create visualizations for data analysis. In this tutorial, we will learn how to use `axvline`, `axhline`, and `axline` to draw infinite lines in Matplotlib.

## Steps

### Step 1: Draw vertical and horizontal lines

We can use `axvline` and `axhline` to draw vertical and horizontal lines respectively. Let's draw three horizontal lines at `y=0`, `y=0.5`, and `y=1.0`.

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate data
t = np.linspace(-10, 10, 100)
sig = 1 / (1 + np.exp(-t))

# Draw horizontal lines
plt.axhline(y=0, color="black", linestyle="--")
plt.axhline(y=0.5, color="black", linestyle=":")
plt.axhline(y=1.0, color="black", linestyle="--")

# Plot sigmoid function
plt.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
plt.xlim(-10, 10)
plt.xlabel("t")
plt.legend(fontsize=14)
plt.show()
```

### Step 2: Draw vertical line

We can use `axvline` to draw a vertical line at a given `x` position. Let's draw a vertical line at `x=0`.

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate data
t = np.linspace(-10, 10, 100)
sig = 1 / (1 + np.exp(-t))

# Draw horizontal lines
plt.axhline(y=0, color="black", linestyle="--")
plt.axhline(y=0.5, color="black", linestyle=":")
plt.axhline(y=1.0, color="black", linestyle="--")

# Draw vertical line
plt.axvline(color="grey")

# Plot sigmoid function
plt.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
plt.xlim(-10, 10)
plt.xlabel("t")
plt.legend(fontsize=14)
plt.show()
```

### Step 3: Draw arbitrary line

We can use `axline` to draw a line in any direction. Let's draw a line with slope `0.25` passing through the point `(0, 0.5)`.

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate data
t = np.linspace(-10, 10, 100)
sig = 1 / (1 + np.exp(-t))

# Draw horizontal lines
plt.axhline(y=0, color="black", linestyle="--")
plt.axhline(y=0.5, color="black", linestyle=":")
plt.axhline(y=1.0, color="black", linestyle="--")

# Draw vertical line
plt.axvline(color="grey")

# Draw arbitrary line
plt.axline((0, 0.5), slope=0.25, color="black", linestyle=(0, (5, 5)))

# Plot sigmoid function
plt.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
plt.xlim(-10, 10)
plt.xlabel("t")
plt.legend(fontsize=14)
plt.show()
```

### Step 4: Draw diagonal lines

We can use `axline` with the `transform` parameter to draw diagonal lines with a fixed slope. Let's draw diagonal grid lines with a fixed slope of `0.5`.

```python
import matplotlib.pyplot as plt
import numpy as np

# Draw diagonal lines
for pos in np.linspace(-2, 1, 10):
    plt.axline((pos, 0), slope=0.5, color='k', transform=plt.gca().transAxes)

plt.ylim([0, 1])
plt.xlim([0, 1])
plt.show()
```

## Summary

In this tutorial, we learned how to draw infinite lines in Matplotlib using `axvline`, `axhline`, and `axline`. We learned how to draw vertical and horizontal lines, arbitrary lines, and diagonal lines with a fixed slope. These functions are useful for marking special data values or for drawing grid lines to aid in data analysis.
