# Violin Plotting with Matplotlib

## Introduction

In this lab, we will learn how to create violin plots using Matplotlib library in Python. Violin plots are used to visualize the distribution of a dataset. These plots are similar to box plots, but instead of showing only the summary statistics, violin plots show the full distribution of the data.

We will use a sample dataset to create violin plots and modify various parameters to observe changes in the plot.

## Steps

### Step 1: Import necessary libraries

We will start by importing the necessary libraries to create the violin plots.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create sample dataset

We will create a sample dataset using numpy library. We will create six datasets with different standard deviations.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# fake data
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]
```

### Step 3: Create custom violin plots

We will create custom violin plots by modifying various parameters. We will create 5 custom violin plots using different parameters.

```python
fig, axs = plt.subplots(nrows=2, ncols=5, figsize=(10, 6))

# Custom violinplot 1
axs[0, 0].violinplot(data, pos, points=20, widths=0.3,
                     showmeans=True, showextrema=True, showmedians=True)
axs[0, 0].set_title('Custom violinplot 1', fontsize=fs)

# Custom violinplot 2
axs[0, 1].violinplot(data, pos, points=40, widths=0.5,
                     showmeans=True, showextrema=True, showmedians=True,
                     bw_method='silverman')
axs[0, 1].set_title('Custom violinplot 2', fontsize=fs)

# Custom violinplot 3
axs[0, 2].violinplot(data, pos, points=60, widths=0.7, showmeans=True,
                     showextrema=True, showmedians=True, bw_method=0.5)
axs[0, 2].set_title('Custom violinplot 3', fontsize=fs)

# Custom violinplot 4
axs[0, 3].violinplot(data, pos, points=60, widths=0.7, showmeans=True,
                     showextrema=True, showmedians=True, bw_method=0.5,
                     quantiles=[[0.1], [], [], [0.175, 0.954], [0.75], [0.25]])
axs[0, 3].set_title('Custom violinplot 4', fontsize=fs)

# Custom violinplot 5
axs[0, 4].violinplot(data[-1:], pos[-1:], points=60, widths=0.7,
                     showmeans=True, showextrema=True, showmedians=True,
                     quantiles=[0.05, 0.1, 0.8, 0.9], bw_method=0.5)
axs[0, 4].set_title('Custom violinplot 5', fontsize=fs)
```

### Step 4: Create more custom violin plots

We will create more custom violin plots using different parameters.

```python
# Custom violinplot 6
axs[1, 0].violinplot(data, pos, points=80, vert=False, widths=0.7,
                     showmeans=True, showextrema=True, showmedians=True)
axs[1, 0].set_title('Custom violinplot 6', fontsize=fs)

# Custom violinplot 7
axs[1, 1].violinplot(data, pos, points=100, vert=False, widths=0.9,
                     showmeans=True, showextrema=True, showmedians=True,
                     bw_method='silverman')
axs[1, 1].set_title('Custom violinplot 7', fontsize=fs)

# Custom violinplot 8
axs[1, 2].violinplot(data, pos, points=200, vert=False, widths=1.1,
                     showmeans=True, showextrema=True, showmedians=True,
                     bw_method=0.5)
axs[1, 2].set_title('Custom violinplot 8', fontsize=fs)

# Custom violinplot 9
axs[1, 3].violinplot(data, pos, points=200, vert=False, widths=1.1,
                     showmeans=True, showextrema=True, showmedians=True,
                     quantiles=[[0.1], [], [], [0.175, 0.954], [0.75], [0.25]],
                     bw_method=0.5)
axs[1, 3].set_title('Custom violinplot 9', fontsize=fs)

# Custom violinplot 10
axs[1, 4].violinplot(data[-1:], pos[-1:], points=200, vert=False, widths=1.1,
                     showmeans=True, showextrema=True, showmedians=True,
                     quantiles=[0.05, 0.1, 0.8, 0.9], bw_method=0.5)
axs[1, 4].set_title('Custom violinplot 10', fontsize=fs)
```

### Step 5: Customize plot appearance

We will customize the appearance of the plot by removing y-axis labels and adding a title to the plot.

```python
for ax in axs.flat:
    ax.set_yticklabels([])

fig.suptitle("Violin Plotting Examples")
fig.subplots_adjust(hspace=0.4)
plt.show()
```

## Summary

In this lab, we learned how to create violin plots using Matplotlib library in Python. We created custom violin plots by modifying various parameters such as number of points, bandwidth of KDE, and quantiles. We also learned how to customize the appearance of the plot by removing y-axis labels and adding a title to the plot.
