# Matplotlib Table Function Lab

## Introduction

In this lab, we will learn how to use the Matplotlib table function to display a table within a plot. We will use a sample dataset to visualize the loss incurred by different natural disasters over the years.

## Steps

### Step 1: Import Required Libraries

We will begin by importing the necessary libraries for the project. We will use the Matplotlib library to create the table.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create the Dataset

Next, we will create a sample dataset to visualize the loss incurred by different natural disasters over the years. We will use a two-dimensional list to store the data and a tuple to store the column names.

```python
data = [[ 66386, 174296,  75131, 577908,  32015],
        [ 58230, 381139,  78045,  99308, 160454],
        [ 89135,  80552, 152558, 497981, 603535],
        [ 78415,  81858, 150656, 193263,  69638],
        [139361, 331509, 343164, 781380,  52269]]

columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
```

### Step 3: Create Row Labels

We will create row labels for the dataset to represent the number of years for which the loss has been recorded. We will use a list comprehension to create the row labels.

```python
rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]
```

### Step 4: Create Color Scheme

We will create a color scheme for the table using the `plt.cm.BuPu` function. We will use a pastel shade of blue and purple colors for the rows.

```python
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
```

### Step 5: Create Vertical Stacked Bar Chart

We will create a vertical stacked bar chart using the `plt.bar` function to represent the loss incurred by different natural disasters over the years. We will use a for loop to iterate over each row of data and plot the bars.

```python
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

y_offset = np.zeros(len(columns))

cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
```

### Step 6: Reverse Colors and Text Labels

We will reverse the colors and text labels of the table to display the last value at the top using the `[::-1]` function.

```python
colors = colors[::-1]
cell_text.reverse()
```

### Step 7: Add Table to the Plot

We will add a table to the bottom of the plot using the `plt.table` function. We will pass the cell text, row labels, row colors, and column labels as parameters to the function.

```python
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
```

### Step 8: Adjust Plot Layout

We will adjust the layout of the plot to make room for the table using the `plt.subplots_adjust` function.

```python
plt.subplots_adjust(left=0.2, bottom=0.2)
```

### Step 9: Add Axis Labels and Title

We will add axis labels and a title to the plot using the `plt.ylabel`, `plt.yticks`, `plt.xticks`, and `plt.title` functions.

```python
values = np.arange(0, 2500, 500)
value_increment = 1000

plt.ylabel(f"Loss in ${value_increment}'s")
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Loss by Disaster')
```

### Step 10: Show Plot

We will display the plot using the `plt.show` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to use the Matplotlib table function to display a table within a plot. We used a sample dataset to visualize the loss incurred by different natural disasters over the years. We followed the following steps:

1. Imported Required Libraries
2. Created the Dataset
3. Created Row Labels
4. Created Color Scheme
5. Created Vertical Stacked Bar Chart
6. Reversed Colors and Text Labels
7. Added Table to the Plot
8. Adjusted Plot Layout
9. Added Axis Labels and Title
10. Showed Plot.
