# Python Matplotlib Tutorial - Stepwise Histograms

## Introduction

Matplotlib is a data visualization library in Python. It is widely used for creating a wide range of visualizations like line plots, scatter plots, bar plots, histograms, and more. This tutorial will focus on creating stepwise histograms using Matplotlib.

## Steps

### Step 1: Import the necessary libraries and modules

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import StepPatch
```

### Step 2: Prepare the data

```python
np.random.seed(0)
h, edges = np.histogram(np.random.normal(5, 3, 5000),
                        bins=np.linspace(0, 10, 20))
```

### Step 3: Create a simple step histogram

```python
plt.stairs(h, edges, label='Simple histogram')
plt.legend()
plt.show()
```

### Step 4: Modify the baseline of the step histogram

```python
plt.stairs(h, edges + 5, baseline=50, label='Modified baseline')
plt.legend()
plt.show()
```

### Step 5: Create a step histogram without edges

```python
plt.stairs(h, edges + 10, baseline=None, label='No edges')
plt.legend()
plt.show()
```

### Step 6: Create a filled histogram

```python
plt.stairs(np.arange(1, 6, 1), fill=True,
              label='Filled histogram\nw/ automatic edges')
plt.legend()
plt.show()
```

### Step 7: Create a hatched histogram

```python
plt.stairs(np.arange(1, 6, 1)*0.3, np.arange(2, 8, 1),
              orientation='horizontal', hatch='//',
              label='Hatched histogram\nw/ horizontal orientation')
plt.legend()
plt.show()
```

### Step 8: Create a StepPatch artist

```python
patch = StepPatch(values=[1, 2, 3, 2, 1],
                  edges=range(1, 7),
                  label=('Patch derived underlying object\n'
                         'with default edge/facecolor behaviour'))
plt.gca().add_patch(patch)
plt.xlim(0, 7)
plt.ylim(-1, 5)
plt.legend()
plt.show()
```

### Step 9: Create stacked histograms

```python
A = [[0, 0, 0],
     [1, 2, 3],
     [2, 4, 6],
     [3, 6, 9]]

for i in range(len(A) - 1):
    plt.stairs(A[i+1], baseline=A[i], fill=True)
plt.show()
```

### Step 10: Compare `.pyplot.step` and `.pyplot.stairs`

```python
bins = np.arange(14)
centers = bins[:-1] + np.diff(bins) / 2
y = np.sin(centers / 2)

plt.step(bins[:-1], y, where='post', label='step(where="post")')
plt.plot(bins[:-1], y, 'o--', color='grey', alpha=0.3)

plt.stairs(y - 1, bins, baseline=None, label='stairs()')
plt.plot(centers, y - 1, 'o--', color='grey', alpha=0.3)
plt.plot(np.repeat(bins, 2), np.hstack([y[0], np.repeat(y, 2), y[-1]]) - 1,
         'o', color='red', alpha=0.2)

plt.legend()
plt.title('step() vs. stairs()')
plt.show()
```

## Summary

This tutorial covered the basics of creating stepwise histograms using Matplotlib. We learned how to create simple step histograms, modify the baseline of histograms, create filled and hatched histograms, and create stacked histograms. We also compared the differences between `.pyplot.step` and `.pyplot.stairs`.
