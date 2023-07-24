# Python Matplotlib Tutorial Lab

## Violin Plot Customization

### Introduction

In this lab, we will learn how to customize violin plots using Matplotlib. Violin plots are a powerful tool for visualizing the distribution and density of data. By customizing the appearance of the plot, we can create more informative and visually appealing visualizations.

### Steps

1. **Create test data:** First, we will create some test data to use for the violin plot. We will use NumPy to generate four arrays of 100 normally distributed values with increasing standard deviations.

```python
# create test data
np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
```

2. **Create a default violin plot:** Next, we will create a default violin plot using Matplotlib's `violinplot` function. This will provide a baseline for comparison when we customize the plot in later steps.

```python
# create default violin plot
fig, ax1 = plt.subplots()
ax1.set_title('Default Violin Plot')
ax1.set_ylabel('Observed Values')
ax1.violinplot(data)
```

3. **Customize the violin plot appearance:** Now we will customize the appearance of the violin plot. First, we will limit what Matplotlib draws by setting the `showmeans`, `showmedians`, and `showextrema` arguments to `False`. Then, we will change the color and opacity of the violin bodies using the `set_facecolor` and `set_alpha` methods. Finally, we will add a simplified representation of a box plot on top of the violin plot, using the `percentile` function from NumPy to calculate the quartiles, medians, and whiskers.

```python
# customize violin plot appearance
fig, ax2 = plt.subplots()
ax2.set_title('Customized Violin Plot')
ax2.set_ylabel('Observed Values')

# create violin plot
parts = ax2.violinplot(
        data, showmeans=False, showmedians=False,
        showextrema=False)

# customize violin bodies
for pc in parts['bodies']:
    pc.set_facecolor('#D43F3A')
    pc.set_edgecolor('black')
    pc.set_alpha(1)

# add box plot
quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)
whiskers = np.array([
    adjacent_values(sorted_array, q1, q3)
    for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
whiskers_min, whiskers_max = whiskers[:, 0], whiskers[:, 1]

inds = np.arange(1, len(medians) + 1)
ax2.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
ax2.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
ax2.vlines(inds, whiskers_min, whiskers_max, color='k', linestyle='-', lw=1)
```

4. **Set axis style:** Finally, we will set the style for the x-axis by specifying the tick labels and limits. We will define a helper function `set_axis_style` to accomplish this.

```python
# set style for the axes
labels = ['A', 'B', 'C', 'D']
set_axis_style(ax2, labels)

def set_axis_style(ax, labels):
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Sample Name')
```

### Summary

In this lab, we learned how to customize the appearance of violin plots using Matplotlib. We created a default violin plot, then modified it by changing the color and opacity of the violin bodies, and adding a simplified box plot representation on top. We also set the style for the x-axis tick labels and limits. By customizing the appearance of the plot, we can create more informative and visually appealing visualizations.
