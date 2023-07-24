# Matplotlib Axis Label Position Lab

## Introduction

In this lab, we will learn how to set the position of axis labels and colorbar labels in Matplotlib. We will use the `set_xlabel`, `set_ylabel`, and `colorbar` methods to set the position of the labels.

## Steps

### Step 1: Import Matplotlib and create a scatter plot

We start by importing Matplotlib and creating a scatter plot.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sc = ax.scatter([1, 2], [1, 2], c=[1, 2])
```

### Step 2: Set the position of the y-axis label

We can set the position of the y-axis label using the `set_ylabel` method. We can set the position to `'top'`, `'center'`, or `'bottom'`. In this example, we will set the position to `'top'`.

```python
ax.set_ylabel('YLabel', loc='top')
```

### Step 3: Set the position of the x-axis label

We can set the position of the x-axis label using the `set_xlabel` method. We can set the position to `'left'`, `'center'`, or `'right'`. In this example, we will set the position to `'left'`.

```python
ax.set_xlabel('XLabel', loc='left')
```

### Step 4: Set the position of the colorbar label

We can set the position of the colorbar label using the `colorbar` method and the `set_label` method. We can set the position to `'top'`, `'bottom'`, `'left'`, or `'right'`. In this example, we will set the position to `'top'`.

```python
cbar = fig.colorbar(sc)
cbar.set_label("ZLabel", loc='top')
```

### Step 5: Display the plot

We can display the plot using the `show` method.

```python
plt.show()
```

## Summary

In this lab, we learned how to set the position of axis labels and colorbar labels in Matplotlib. We used the `set_xlabel`, `set_ylabel`, and `colorbar` methods to set the position of the labels. We also learned that we can set the position to `'top'`, `'bottom'`, `'left'`, `'right'`, `'center'`, or `'baseline'`.
