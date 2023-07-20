# Matplotlib Plot Title Positioning Lab

## Introduction

In this lab, you will learn how to position the titles of plots in Matplotlib. Matplotlib can display plot titles centered, flush with the left side of a set of axes, and flush with the right side of a set of axes. This lab will show you how to use Matplotlib to position plot titles in different ways.

## Steps

### Step 1: Create a Basic Plot

First, import the Matplotlib library and create a basic plot using the `plot()` function.

```python
import matplotlib.pyplot as plt
plt.plot(range(10))
```

### Step 2: Center Title

Add a centered title to the plot using the `title()` function.

```python
plt.title('Center Title')
```

### Step 3: Left Title

Add a title aligned to the left side of the plot using the `title()` function and the `loc` parameter.

```python
plt.title('Left Title', loc='left')
```

### Step 4: Right Title

Add a title aligned to the right side of the plot using the `title()` function and the `loc` parameter.

```python
plt.title('Right Title', loc='right')
```

### Step 5: Top Title

Create a plot with the title at the top using the `subplots()` function and the `set_xlabel()` function.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Top Title')
```

### Step 6: Manual Y Positioning

Manually specify the vertical position of the title by using the `y` parameter of the `title()` function.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Manual Y Positioning', y=1.0)
```

### Step 7: RCParam Y Positioning

Set the `titley` and `titlepad` parameters of the `rcParams` to adjust the vertical positioning of the title.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
plt.rcParams['axes.titley'] = 1.0
plt.rcParams['axes.titlepad'] = -14
ax.set_title('RCParam Y Positioning')
```

## Summary

In this lab, you learned how to position plot titles in Matplotlib. You can center the title using the `title()` function, align it to the left or right using the `loc` parameter, or position it at the top using the `set_xlabel()` function. You can also manually specify the vertical position using the `y` parameter or adjust it using the `titley` and `titlepad` parameters of the `rcParams`.
