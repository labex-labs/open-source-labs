# Text Annotations in 3D

## Introduction

This lab will demonstrate how to place text annotations on a 3D plot using Matplotlib library in Python. The following functionalities will be covered:

- Using the `~.Axes3D.text` function with three types of _zdir_ values: None, an axis name (ex. 'x'), or a direction tuple (ex. (1, 1, 0)).
- Using the `~.Axes3D.text` function with the color keyword.
- Using the `.text2D` function to place text on a fixed position on the ax object.

## Steps

### Step 1: Import Libraries

Import the necessary libraries to create a 3D plot and add text annotations.

```python
import matplotlib.pyplot as plt
```

### Step 2: Create a 3D Plot

Create a 3D plot using the `add_subplot` method.

```python
ax = plt.figure().add_subplot(projection='3d')
```

### Step 3: Using `~.Axes3D.text` Function with `zdir` Values

Use the `~.Axes3D.text` function to place text annotations with different `zdir` values.

```python
zdirs = (None, 'x', 'y', 'z', (1, 1, 0), (1, 1, 1))
xs = (1, 4, 4, 9, 4, 1)
ys = (2, 5, 8, 10, 1, 2)
zs = (10, 3, 8, 9, 1, 8)

for zdir, x, y, z in zip(zdirs, xs, ys, zs):
    label = '(%d, %d, %d), dir=%s' % (x, y, z, zdir)
    ax.text(x, y, z, label, zdir)
```

### Step 4: Using `~.Axes3D.text` Function with `color` Keyword

Use the `~.Axes3D.text` function with the `color` keyword to change the color of the text annotation.

```python
ax.text(9, 0, 0, "red", color='red')
```

### Step 5: Using `.text2D` Function

Use the `.text2D` function to place text annotations on a fixed position on the `ax` object.

```python
ax.text2D(0.05, 0.95, "2D Text", transform=ax.transAxes)
```

### Step 6: Tweaking Display Region and Labels

Tweak the display region and labels of the 3D plot.

```python
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
```

### Step 7: Display the Plot

Display the 3D plot with text annotations.

```python
plt.show()
```

## Summary

This lab demonstrated how to place text annotations on a 3D plot using Matplotlib library in Python. The `~.Axes3D.text` function with different `zdir` values and `color` keyword, as well as the `.text2D` function, were used to place text annotations in the 3D plot. The display region and labels of the 3D plot were also customized.
