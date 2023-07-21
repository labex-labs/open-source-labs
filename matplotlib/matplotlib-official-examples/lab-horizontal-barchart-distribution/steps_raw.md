# Step-by-Step Lab: Discrete Distribution as Horizontal Bar Chart

## Introduction

In this lab, we will learn how to visualize discrete distributions using horizontal stacked bar charts. We will use Matplotlib, a popular plotting library in Python, to create a survey results visualization.

## Steps

### Step 1: Import Libraries

First, we will import the necessary libraries. We will use Matplotlib and Numpy in this lab.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Prepare Data

We need to define the categories and survey results. In this example, we have a survey where people rated their agreement to questions on a five-element scale. We will define the categories as `category_names` and the survey results as `results`.

```python
category_names = ['Strongly disagree', 'Disagree',
                  'Neither agree nor disagree', 'Agree', 'Strongly agree']
results = {
    'Question 1': [10, 15, 17, 32, 26],
    'Question 2': [26, 22, 29, 10, 13],
    'Question 3': [35, 37, 7, 2, 19],
    'Question 4': [32, 11, 9, 15, 33],
    'Question 5': [21, 29, 5, 5, 40],
    'Question 6': [8, 19, 5, 30, 38]
}
```

### Step 3: Define Function

Now, we will define a function called `survey` that takes in the `results` and `category_names` and creates a horizontal stacked bar chart visualization.

```python
def survey(results, category_names):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    # Convert the results and categories to numpy arrays
    labels = list(results.keys())
    data = np.array(list(results.values()))

    # Calculate cumulative sums of data for horizontal stacking
    data_cum = data.cumsum(axis=1)

    # Define category colors
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    # Create the plot and set axis properties
    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    # Create the stacked bars and add bar labels
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)

    # Add legend
    ax.legend(ncols=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax
```

### Step 4: Call Function and Display Results

Finally, we will call the `survey` function with the `results` and `category_names` as inputs and display the resulting visualization.

```python
survey(results, category_names)
plt.show()
```

## Summary

In this lab, we learned how to create a horizontal stacked bar chart to visualize discrete distributions using Matplotlib. We defined the categories and survey results, created a function to generate the plot, and displayed the results. This technique can be useful for visualizing survey results or other types of discrete distributions.
