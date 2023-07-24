# Python Matplotlib Tutorial

## Introduction

Matplotlib is a Python library used for creating static, animated, and interactive visualizations in Python. It is a popular library used for data visualization in Python. In this tutorial, we will learn how to create a broken horizontal bar plot using Matplotlib.

## Steps

### Step 1: Import the necessary libraries

In this step, we will import the necessary libraries. We will be using the `matplotlib.pyplot` library to create the broken horizontal bar plot.

```python
import matplotlib.pyplot as plt
```

### Step 2: Create the broken horizontal bar plot

In this step, we will create the broken horizontal bar plot. We will be using the `broken_barh()` method of the `Axes` class to create the plot. The `broken_barh()` method takes three arguments: the first argument is a list of tuples where each tuple represents a segment of the bar and the first element of the tuple is the starting point of the segment and the second element is the length of the segment; the second argument is the y-coordinate of the bar; and the third argument is the face color of the bar.

```python
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='tab:blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_ylim(5, 35)
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
ax.set_yticks([15, 25], labels=['Bill', 'Jim'])
ax.grid(True)
ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()
```

### Step 3: Interpret the plot

In this step, we will interpret the broken horizontal bar plot. The plot represents a race where two participants, Bill and Jim, started at different times. The y-axis represents the participants, and the x-axis represents the time since the start of the race in seconds. The blue and orange bars represent Bill's race, while the green, red, and light blue bars represent Jim's race. The annotation "race interrupted" indicates that the race was interrupted at 61 seconds.

## Summary

Matplotlib is a popular library used for data visualization in Python. In this tutorial, we learned how to create a broken horizontal bar plot using Matplotlib. We imported the necessary libraries, created the plot using the `broken_barh()` method of the `Axes` class, and interpreted the plot.
