# Adding Lines to Figures - Step-by-Step Lab

## Introduction

In this lab, we will learn how to add lines to a figure without any axes using Matplotlib in Python.

## Steps

### Step 1: Import necessary libraries

First, we need to import the necessary libraries. We will be using `matplotlib.pyplot` and `matplotlib.lines` for this lab.

```python
import matplotlib.pyplot as plt
import matplotlib.lines as lines
```

### Step 2: Create a Figure object

Next, we create a `Figure` object using the `plt.figure()` method.

```python
fig = plt.figure()
```

### Step 3: Add lines to the Figure

We can add lines to the figure using the `fig.add_artist()` method. We will create two lines - one from (0,0) to (1,1) and another from (0,1) to (1,0).

```python
fig.add_artist(lines.Line2D([0, 1], [0, 1]))
fig.add_artist(lines.Line2D([0, 1], [1, 0]))
```

### Step 4: Display the Figure

Finally, we display the figure using the `plt.show()` method.

```python
plt.show()
```

## Summary

In this lab, we learned how to add lines to a figure without any axes using Matplotlib in Python. We used `matplotlib.pyplot` and `matplotlib.lines` libraries to create a `Figure` object and add lines to it using `fig.add_artist()` method. We then displayed the figure using `plt.show()` method.
