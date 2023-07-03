# Python Matplotlib Tutorial Lab

## Text Watermark

### Introduction

In this lab, we will learn how to add a text watermark effect to a matplotlib plot.

### Steps

#### Step 1: Import Necessary Libraries

Before we start, we need to import the necessary libraries. In this lab, we will be using `numpy` and `matplotlib`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

#### Step 2: Generate Data

Let's generate some random data to plot.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(np.random.rand(20), '-o', ms=20, lw=2, alpha=0.7, mfc='orange')
ax.grid()
```

#### Step 3: Add Text Watermark

To add a text watermark, we can use the `text()` method of the `Figure` object. We need to provide the position, text, and other properties like font size, color, and transparency.

```python
ax.text(0.5, 0.5, 'created with matplotlib', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation=30)
```

#### Step 4: Display the Plot

Finally, we can display the plot using the `show()` method.

```python
plt.show()
```

### Summary

In this lab, we learned how to add a text watermark effect to a matplotlib plot. We imported the necessary libraries, generated random data, added the text watermark using the `text()` method, and displayed the plot using the `show()` method.
