# Python Matplotlib Tutorial

## Introduction

This tutorial will guide you through the process of creating box plot and violin plot using Python Matplotlib library. Box plots and violin plots are used to visualize the distribution of data.

## Steps

### Step 1: Import libraries

Before creating the plots, we need to import the necessary libraries. We will be using `numpy` to generate random data and `matplotlib.pyplot` to create the plots.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate data

We will generate some random test data using numpy.

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]
```

### Step 3: Create violin plot

We will create a violin plot using `violinplot()` method. This method takes multiple arguments such as data, showmeans, showmedians etc.

```python
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
axs[0].violinplot(all_data, showmeans=False, showmedians=True)
axs[0].set_title('Violin plot')
```

### Step 4: Create box plot

We will create a box plot using `boxplot()` method. This method takes multiple arguments such as data, labels, showmeans, notch etc.

```python
axs[1].boxplot(all_data)
axs[1].set_title('Box plot')
```

### Step 5: Add grid lines and labels

We will add horizontal grid lines, set x-labels and y-labels to the plots.

```python
for ax in axs:
    ax.yaxis.grid(True)
    ax.set_xticks([y + 1 for y in range(len(all_data))], labels=['x1', 'x2', 'x3', 'x4'])
    ax.set_xlabel('Four separate samples')
    ax.set_ylabel('Observed values')
```

### Step 6: Display the plots

Finally, we will display the plots using `show()` method.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to create box plot and violin plot using Python Matplotlib library. We also learned how to add horizontal grid lines, set x-labels and y-labels to the plots. Box plots and violin plots are useful in visualizing the distribution of data.
