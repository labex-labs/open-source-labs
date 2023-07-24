# The Lifecycle of a Plot

## Introduction

In this lab, we will explore the lifecycle of a plot using Matplotlib. We will start with raw data and end by saving a customized visualization. We will learn how to create a plot, control its style, customize its appearance, combine multiple visualizations, and save the plot to disk.

## Steps

### Step 1: Import the necessary modules

First, we need to import the required modules: Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Prepare the data

We will use a sample dataset that contains sales information for different companies. Here is an example of the data:

```python
data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)
```

### Step 3: Create the plot

We will use the barplot visualization to represent the sales data. Follow these steps:

1. Create a figure and an axis object using `plt.subplots()`.

```python
fig, ax = plt.subplots()
```

2. Plot the data using the `barh()` method of the axis object.

```python
ax.barh(group_names, group_data)
```

### Step 4: Customize the plot style

We can change the style of our plot to make it more visually appealing. Follow these steps:

1. Print the list of available styles using `print(plt.style.available)`.

```python
print(plt.style.available)
```

2. Choose a style and apply it using `plt.style.use(style_name)`.

```python
plt.style.use('fivethirtyeight')
```

### Step 5: Customize the plot appearance

We can further customize the appearance of our plot. Follow these steps:

1. Rotate the x-axis labels to make them more readable.

```python
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
```

2. Set the x-axis and y-axis limits, labels, and title.

```python
ax.set(xlim=[-10000, 140000],
       xlabel='Total Revenue',
       ylabel='Company',
       title='Company Revenue')
```

### Step 6: Combine multiple visualizations

We can add additional plot elements to our visualization. Follow these steps:

1. Add a vertical line representing the mean of the sales data.

```python
ax.axvline(group_mean, ls='--', color='r')
```

2. Annotate new companies on the plot.

```python
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10, verticalalignment="center")
```

3. Adjust the position of the plot title.

```python
ax.title.set(y=1.05)
```

### Step 7: Save the plot

Finally, we can save our plot to disk. Follow these steps:

1. Print the supported file formats using `print(fig.canvas.get_supported_filetypes())`.

```python
print(fig.canvas.get_supported_filetypes())
```

2. Save the figure as an image file using `fig.savefig(file_path, transparent=False, dpi=80, bbox_inches="tight")`. Uncomment this line to save the figure.

```python
fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
```

## Summary

In this lab, we learned about the lifecycle of a plot using Matplotlib. We started by creating a plot, controlling its style, customizing its appearance, combining multiple visualizations, and saving the plot to disk. Matplotlib offers a wide range of customization options to create visually appealing and informative plots.
